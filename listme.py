import re

def extract_field_strings(content):
    # Regular expression to match field('string', *)
    field_pattern = re.compile(r"field\(\s*'([^']+)'")

    # Find all matches in the content
    matches = field_pattern.findall(content)

    return matches

# Read the content of the file
file_path = 'grammar.js'
with open(file_path, 'r') as file:
    content = file.read()

# Extract field strings
field_strings = extract_field_strings(content)
field_strings

