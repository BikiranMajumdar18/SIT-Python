''' Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic
salary, and house rent allowance is 20% of basic salary. Write a program to calculate his
gross salary. '''

BS = int(input("Enter Basic Salary "))
DA = BS * 40 / 100
HRA = BS * 20 / 100
GS = BS + DA + HRA
print(GS)
