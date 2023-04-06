# Task 1

sentence = input('Введите предложение: ')
chars_popularity = {}
words_popularity = {}

for symbol in sentence:
    chars_popularity[symbol] = sentence.count(symbol)

for word in sentence.split():
    words_popularity[word] = sentence.count(word)

print(words_popularity)
print(chars_popularity, '\n')

# Task 2

rates = {'Sberbank': 55.8, 'VTB24': 53.91, 'Tinkoff': 56.4, 'Alfa': 53.8}
min_value = min(rates.values())
for key in rates.keys():
    if rates[key] == min_value:
        print(f'{key} -> {min_value}\n')
        break
# Task 3

dates = ['2017-03-01', '2017-03-02', '2023-04-23', '2018-30-01']
rates = [55.7, 55.2, 87.9, 65.1]
new_dict = {}
while dates and rates:
    new_dict[dates[0]] = rates[0]
    dates.pop(0)
    rates.pop(0)
print(new_dict)
