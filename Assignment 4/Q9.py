''' Write a program to accept the strings which contain all vowels '''

input_str = input("Enter a string: ")

vowels = set("aeiou")

x = input_str.lower()

if vowels.issubset(set(x)):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
