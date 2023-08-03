import sys
import re

if len(sys.argv) != 2:
    sys.exit("Usage: python program.py file.py")

file_name = sys.argv[1]
if not file_name.endswith(".py"):
    sys.exit("File must be a Python file")

try:
    with open(file_name, "r") as file:
        code = file.read()
        # Remove comments
        code = re.sub(r"(#.*|\s+#.*)", "", code)
        # Split into lines and filter out empty lines
        lines = [line.strip() for line in code.split("\n") if line.strip()]
        number_of_lines = len(lines)
        print(number_of_lines)
except FileNotFoundError:
    sys.exit("File does not exist")



