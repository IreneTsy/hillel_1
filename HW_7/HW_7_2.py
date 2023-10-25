'''Завдання 2 (опціонально +2 до роботи)

Створіть словник із випадковими числовими значеннями довжиною в
20 елементів. Необхідно їх (числові значення) перемножити і вивести
на екран згенерований на початку словникта результат множення чисел.'''

import random
from collections import OrderedDict

dict_one = {}
mult = 1
rng = 20

for i in range(rng):
    dict_one.setdefault(i, [])
    r = random.randint(1, 10)
    dict_one[i].append(r)
    mult = mult * r
dict_one[rng] = [mult]
dct = OrderedDict(sorted(dict_one.items(), key=lambda t: t[1]))
dct.move_to_end(20, last=False)
print(dct)
