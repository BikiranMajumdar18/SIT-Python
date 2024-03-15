''' Write a program to take input a string of digits and convert it to an integer without
using int() function. '''

input_string = input("Enter a string ")
print(type(input_string))

result = 0

for digit in input_string:
    digit_value = ord(digit) - ord('0')
    result = result * 10 + digit_value

print("converted_integer", result)
print(type(result))
