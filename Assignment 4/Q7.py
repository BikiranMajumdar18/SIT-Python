''' Write a program to capitalize the first and last character of each word in a string '''

string_input = input("Enter a string: ")

words = string_input.split()

modified_words = []

for word in words:
    if len(word) > 1:
        modified_word = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        modified_word = word.upper()
    
    modified_words.append(modified_word)

result = ' '.join(modified_words)
print("The modified string is:", result)
