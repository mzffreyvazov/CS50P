import csv
import sys
import os.path

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3 and not os.path.isfile(sys.argv[1]):
    sys.exit(f"Could not read {sys.argv[1]}")

input_file = sys.argv[1]
output_file = sys.argv[2]
output = []
try:
    with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create name, last name
                split_name = row['name'].split(",")
                # Add them to dict
                output.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row['house']})
    # Write new csv file
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row['first'], "last": row['last'], "house": row['house']})

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")
except ValueError:
    sys.exit(f"Error reading {input_file}")


