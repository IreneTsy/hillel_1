import random

#Задаємо на вхід довільні параметри"
def create_2d_arrays(*args):
 #   """Ф-ція якщо параметр не введений"""
    if len(args) == 0:
        print(None)

#"""Ф-ція для одного параметру"""
    elif len(args) == 1:
#"""Генерація 2 вимірного списку з одним параметром, що заповнені
# випадковими цілими значенням в диапазлні 0 - 200"""
        matrix = [ 
          [random.randint(0, 200) for _ in range(args[0])]
            for __ in range(args[0])
        ]
#"""Визначення максимальної довжини рядка для формувння симетричної таблички"""
        max_len = max(len(str(max(row)) if row else 0) for row in matrix)
        for row in matrix:
            formatted_row = [f'{val:^{max_len}}' for val in row]
#"""Виведення відформатованого списку по рядкам"""
            print(' '.join(formatted_row))

#"""Ф-ція для двох параметрів"""
    elif len(args) == 2:
        matrix = [
            [random.randint(0, 200) for _ in range(args[0])]
            for __ in range(args[1])
        ]
#""Визначення максимальної довжини рядка для формувння симетричної таблички"""
        max_len = max(len(str(max(row)) if row else 0) for row in matrix)
        for row in matrix:
            formatted_row = [f'{val:^{max_len}}' for val in row]
            print(' '.join(formatted_row))

print(create_2d_arrays())
print(create_2d_arrays(5))
print(create_2d_arrays(4, 7))
