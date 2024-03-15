''' WAP to print even length words in a string. '''

string = input("Enter any string ")
words = string.split(' ')
even_length_words = []

for word in words:
    if len(word) % 2 == 0:
        even_length_words.append(word)

result = ' '.join(even_length_words)
print(result)