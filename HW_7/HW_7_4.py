'''Завдання 4 (опціонально +5 до роботи)

Дано два списки однакової довжини. Необхідно створити з них
словник таким чином, щоб елементи першого списку були ключами,
а елементи другого відповідно значеннями нашого словника.'''

a = ['Name', 'Surname', 'Age', 'Gender', 'Country']
b = ['Alex', 'Smith', '35', 'Male', 'USA']
prof = dict(zip(a, b))
print(prof)