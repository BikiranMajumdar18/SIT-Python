''' Write a program to remove all duplicates from a given string in Python, keeping the
first character only '''

input_str = "programming"

seen = set()
output_str = ""

for char in input_str:
    if char not in seen:
        output_str = output_str + char
        seen.add(char)

print(output_str)
