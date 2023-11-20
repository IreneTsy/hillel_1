def input_function():
    try:
        # Запитуємо введення двох значень
        value_1 = input("Введіть перше значення: ")
        value_2 = input("Введіть друге значення: ")

        # Спробуємо перетворити їх на числа
        num_1 = float(value_1)
        num_2 = float(value_2)

        # Якщо обидва значення є числами, розраховуємо суму
        return num_1 + num_2
    except ValueError:
        # Якщо хоча б одне із значень не є числом, виконуємо конкатинацію
        return value_1 + value_2

# Перевірка функції
result = input_function()
print(result)