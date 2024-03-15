''' WAP to remove i^th character of a string. ''' 

string_input = input("Enter a string: ")
i = int(input("Enter the index of the character to remove: "))

if 0 <= i < len(string_input):
    updated_string = string_input[:i] + string_input[i+1:]
    print(f"The string after removing the {i}-th character is:" , updated_string)
else:
    print("Invalid index. Please enter a valid index.")
