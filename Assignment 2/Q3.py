'''Any year is input through the keyboard. Write a program to determine whether 
the year is a leap year or not.'''

yr = int(input("Enter a year: "))

if (yr%4 == 0 and yr%100 != 0) or (yr%400 == 0):
        print("Leap year")
else:
        print("Not a leap year")
