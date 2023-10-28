import random

int_elements = [random.randint(1, 500) for _ in range(25)]
print(int_elements)

print('Список, що складається із квадратів int_elements',
      [x ** 2 for x in int_elements])

print('Список, що складається із остач ділення на 11 елементів',
      [x % 11 for x in int_elements])

print('Список, що складається лише з парних елементів',
      [x for x in int_elements if x%2 == 0])

print('Список, що складається лише з елементів з непарною кількістю цифр',
      [x for i, x in enumerate(int_elements) if i%3 == 0 and i != 0])

print('Список з непарною кількістю цифр:',
      [x for x in int_elements if (len(str(x)))%2])