import sys
from PIL import Image, ImageOps

# Check that exactly two arguments were provided
if len(sys.argv) != 3:
    sys.exit("Error: Expected exactly two arguments")

# Check that the input and output files have valid extensions
valid_extensions = ['.jpg', '.jpeg', '.png']
input_filename = sys.argv[1]
output_filename = sys.argv[2]
if not any(input_filename.lower().endswith(ext) for ext in valid_extensions):
    sys.exit("Error: Input file must have a .jpg, .jpeg, or .png extension")
if not any(output_filename.lower().endswith(ext) for ext in valid_extensions):
    sys.exit("Error: Output file must have a .jpg, .jpeg, or .png extension")

# Check that the input and output files have the same extension
if input_filename.split('.')[-1].lower() != output_filename.split('.')[-1].lower():
    sys.exit("Error: Input and output files must have the same extension")

# Check that the input file exists
try:
    with open(input_filename, 'rb'):
        pass
except FileNotFoundError:
    sys.exit(f"Error: Input file '{input_filename}' does not exist")

# Open the input file and get its dimensions
with Image.open(input_filename) as im:
    input_width, input_height = im.size

    # Open the shirt image
    shirt = Image.open('shirt.png')

    # Resize and crop the input image to be the same size as the shirt
    input_resized = ImageOps.fit(im, (shirt.width, shirt.height))

    # Overlay the shirt onto the input image
    input_resized.paste(shirt, mask=shirt)

    # Save the result as the output file
    input_resized.save(output_filename)
