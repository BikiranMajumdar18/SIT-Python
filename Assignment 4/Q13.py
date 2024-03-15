''' Write a program to maximum frequency character in String ''' 

input_str = "cickhead"
char_count = {}
most_frequent_char = None
max_count = 0

for char in input_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

    if char_count[char] > max_count:
        max_count = char_count[char]
        least_frequent_char = char

print("Maximum frequent character:", least_frequent_char)
print("Count:", max_count)
