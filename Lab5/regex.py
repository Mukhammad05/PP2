# task 1
import re

word = input("Enter a string: ")

match = re.match(r'ab*', word)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")


# task 2
import re

input_str = input("Enter a string: ")
pattern = r'a(bb{2,3})'

if re.search(pattern, input_str):
    print("String matches the pattern.")
else:
    print("String does not match the pattern.")


# task 3
import re

text = str(input("Enter string: "))

pattern = r'\b[a-z]+_[a-z]+\b'

matches = re.findall(pattern, text)

print("Sequences of lowercase letters joined with an underscore:")
for match in matches:
    print(match)


# task 4
import re

text = str(input("Enter string: "))

pattern = r'[A-Z][a-z]+'

matches = re.findall(pattern, text)

print("Sequences of one upper case letter followed by lower case letters:")
print(matches)


# task 5
import re

text = str(input("Enter string: "))

pattern = r'a.*b$'

if re.search(pattern, text):
    print("String matches the pattern.")
else:
    print("String does not match the pattern.")

# task 6
import re

text = str(input("Enter string: "))

pattern = r'[ ,.]'

output_text = re.sub(pattern, ':', text)

print(output_text)

# task 7
import re

snake_case_string = str(input("Enter string: "))

camel_case_string = re.sub(r'_([a-zA-Z])', lambda x: x.group(1).upper(), snake_case_string)

print("Snake case:", snake_case_string)
print("Camel case:", camel_case_string)

# task 8
import re

input_string = str(input("Enter string: "))

split_strings = re.findall('[A-Z][^A-Z]*', input_string)

for split_string in split_strings:
    print(split_string)

# task 9
import re

input_string = str(input("Enter string: "))

output_string = re.sub(r'(?<!^)([A-Z])', r' \1', input_string)

print(output_string)

# task 10
import re

camel_case_string = str(input("Enter string: "))

snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()

print("Camel case:", camel_case_string)
print("Snake case:", snake_case_string)














