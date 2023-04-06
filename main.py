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

rates = {'Sberbank': 55.8, 'VTB24': 53.91, 'Tinkoff': 56.4, 'Alfa': 53.8}
min_value = min(rates.values())
for key in rates.keys():
    if rates[key] == min_value:
        print(f'{key} -> {min_value}')