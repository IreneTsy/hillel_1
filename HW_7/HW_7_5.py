'''Завдання 5

Створіть словник з рядка 'Python is good language to learn and
in same time we like to tell that it is cool expereance for us' наступним чином:
як ключі візьміть літери рядка, а значеннями нехай будуть числа, що відповідають
кількості входження даної літери в рядок.'''

my_string = 'Python is good language to learn and in same time we like to tell that it is cool experience for us'
my_string = my_string.lower()
my_dct = {}
char_2 = [*my_string]
for i in char_2:
    my_dct.setdefault(i, 0)
    my_dct[i] += 1
del my_dct[' ']
print(my_dct)