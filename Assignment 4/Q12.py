''' Write a program to least Frequent Character in String '''

input_str = "dickhead"
char_count = {}
least_frequent_char = None
min_count = float('inf')

for char in input_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
        
'''
    if char_count[char] < min_count:
        min_count = char_count[char]
        least_frequent_char = char

print("Least frequent character:", least_frequent_char)
print("Count:", min_count)''' 

print(char_count)