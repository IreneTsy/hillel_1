#A. 
#1.Заміна значень 2х змінних використовючи 3-тю змінну - рузультат вивести на/в термінал
x = 25
y = 98
z = x
x = y
y = z
print(x)
print(y)

# 2.заміна значень 2х змінних використовуючи властивості python - рузультат вивести на/в термінал
x, y = y, x
print(x)
print(y)

# 3. Заміна значень 2 змінних не використівуючи 2х попредніх варіантів
x = x + y
y = x - y
x = x - y
print(x)
print(y)

#B.
name = input("Ваше ім'я: ")
surname = input("Ваше призвіще: ")
age = int(input("Ваш вік: "))
print(name)
print(surname)
print(age)
digit = int(input('Введіть 5 значне число -> : '))
left, right = divmod(digit, 10000)
print('тисячі :', right)
left, right = divmod(digit, 100)
print ('сотені :', left)
left, right = divmod(digit, 10)
print('десятки :', left)
left, right = divmod(digit, 1)
print('одиниці :', left)
print('трійок у числі :', digit//3)
print('шісток у числі :', digit//6)


