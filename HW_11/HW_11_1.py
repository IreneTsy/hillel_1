# Функція для обчислення гіпотенузи
def hypotenuse(x, y=1):
    return (x ** 2 + y ** 2) ** 0.5

# Отримання одного списку чисел
numbers = (3, 4, 5)
res_1 = (
    list(
    map(lambda x: hypotenuse(x), numbers)
        )
        )
print("Гіпотенузи з одним параметром x:", res_1)

# Отримання двох списків чисел
x = [6, 8, 10]
y = [8, 15, 17]
res_2 = list(
    map(lambda x, y: hypotenuse(x, y), x, y)
    )
print("Гіпотенузи з двома параметрами - x та y:", res_2)