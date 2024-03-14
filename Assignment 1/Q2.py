''' The distance between two cities (in km.) is input through the keyboard. Write a program to
convert and print this distance in meters, feet, inches and centimeters.''' 

km = (int(input("Enter the value in km: ")))
m = km*1000
print("Distance in meter: ", m)
ft = km*3280.24
print("Distance in feet: ", ft)
