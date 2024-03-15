''' Python program to check if a string has at least one letter and one number '''

string_input = input("Enter a string: ")

has_letter = False
has_number = False

for char in string_input:
    if char.isalpha():
        has_letter = True
    elif char.isdigit():
        has_number = True

if has_letter and has_number:
    print("The string contains at least one letter and one number.")
else:
    print("The string doesn't contain both a letter and a number.")
