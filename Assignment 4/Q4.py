''' WAP to calculate the length of a string, avoid space. ''' 

string_input = input("Enter a string: ")

length_without_spaces = 0

for char in string_input:
    if char != ' ':
        length_without_spaces = length_without_spaces + 1

print("The length of the string without spaces is:" , length_without_spaces)
