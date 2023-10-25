'''Завдання 1

Дано два словники: dictionary_1 = {'a': 300, 'b': 400}
і dictionary_2 = {'c': 500, 'd': 600}. Об'єднайте їх за допомогою вбудованих функцій мови Python.'''

dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)