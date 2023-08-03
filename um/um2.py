import re

# Compile the regular expression pattern
pattern = re.compile(r"\bcat\b")

# Use the findall method to find all occurrences of the pattern in a string
result = pattern.findall("The cat in the cat sat on the cat")

# Print the result
print(result)  # Output: ['cat']

# Use the finditer method to find all occurrences of the pattern and
# return an iterator of match objects
