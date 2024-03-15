''' Write a program to take binary input numbers and convert it to an integer without
using int() function. '''

binary_input = input("Enter a binary number: ")

decimal_result = 0
power = 0

for digit in binary_input[::-1]:
    if digit == '1':
        decimal_result = decimal_result + 2 ** power
    power = power + 1

print("The decimal equivalent is", decimal_result)
