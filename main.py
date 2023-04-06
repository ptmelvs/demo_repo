# Task 1

sentence = input('Введите предложение: ')
chars_popularity = {}
words_popularity = {}

for symbol in sentence:
    chars_popularity[symbol] = sentence.count(symbol)

for word in sentence.split():
    words_popularity[word] = sentence.count(word)

print(words_popularity)
print(chars_popularity)

# Task 2