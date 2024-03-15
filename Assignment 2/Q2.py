'''Any integer is input through the keyboard. Write a program to find out whether 
it is an odd number or even number.'''

n = int(input("Enter the number: "))

if n % 2 == 0:
    print(n,"is an even number")
else:
    print(n,"is an odd number")
