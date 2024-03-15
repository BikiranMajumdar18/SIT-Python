''' Write a program to count the Number of matching characters in a pair of string '''

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

common_characters = set(string1) & set(string2)
print("Number of matching characters:" , len(common_characters))