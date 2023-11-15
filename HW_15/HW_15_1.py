class Triangle:

    def __init__(self, a, b, c):
        # Викликаємо значення трикутника
        self.a = a
        self.b = b
        self.c = c


class TriangleChecker(Triangle):
    def is_triangle(self):
        # Перевіряємо чи значення сторін є числами
        if not all(isinstance(el, (int, float)) for el in [self.a, self.b, self.c]):
            return "Потрібно вводити тільки числа!"

        # Перевіряємо чи всі значення більші за нуль
        if any(el <= 0 for el in [self.a, self.b, self.c]):
            return "З негативними числами нічого не вийде!"

        # Перевіряємо, щоб сума двох сторін трикутника була більшою
        # за сторону третьої сторони
        if self.a + self.b > self.c and \
                self.b + self.c > self.a and \
                self.c + self.a > self.b:
            return "Ура, можна побудувати трикутник!"

        else:
            return "Жаль, але з цього трикутник не зробити."


class ExtTriangle(TriangleChecker, Triangle):
    # Визначаємо наслідування ExtTriangle двом попереднім класам
    pass


# Введемо всі значення правильно
triang_1 = ExtTriangle(4, 4, 7)
print(triang_1.is_triangle(), ' -- Введемо всі значення правильно')

# Одна зі сторін містить від'ємне значення
triang_2 = ExtTriangle(4, -4, 7)
print(triang_2.is_triangle(), " -- Одна зі сторін містить від'ємне значення")

# Одна зі сторін має тип str
triang_3 = ExtTriangle(4, 't', 7)
print(triang_3.is_triangle(), ' -- Одна зі сторін має тип str')

# Сума сторін не завжди більша за третю сторону
triang_4 = ExtTriangle(1, 2, 3)
print(triang_4.is_triangle(), ' -- Сума сторін не завжди більша'
                              'за третю сторону')