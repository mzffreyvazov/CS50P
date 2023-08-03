import sys
import os.path
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len (sys.argv) == 2 and not sys.argv[1].endswith('.csv'):
    sys.exit("Not a CSV file")
elif len (sys.argv) == 2 and not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exist")

# read in the CSV file of pizza prices
with open(sys.argv[1]) as f:
    reader = csv.reader(f)
    header = next(reader) # skip the header row
    rows = [row for row in reader]

# format the table using the tabulate library
print(tabulate(rows, headers=header, tablefmt='grid'))
