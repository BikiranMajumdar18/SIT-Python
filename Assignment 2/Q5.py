'''A five-digit number is entered through the keyboard. Write a program to obtain 
the reversed number and to determine whether the original and reversed numbers 
are equal or not.'''

s = 0
n = int(input("Enter a five-digit number: "))
temp = n

while n != 0:
    r = n % 10
    s = s * 10 + r
    n = n // 10

if temp == s:
    print("Reversed no. is same as original")
else:
    print("Reversed no. is not same as original")
