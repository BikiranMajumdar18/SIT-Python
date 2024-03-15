''' Write a program uppercase Half String. ''' 

string = input("Enter any string ")
mid_point = len(string) // 2

modified_string = string[:mid_point].upper() + string[mid_point:]
print(modified_string)