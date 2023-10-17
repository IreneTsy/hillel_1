lst = []

while True:
    n = int(input("Введіть число: "))
    lst.append(n)
    i =+ 1
    if n == 0:
        break
lst_1 = lst.pop()
print("Сума всіх введених чисел ", sum(lst))
print("Середнє арифметичне усіх введених чисел (не враховуючи останнього 0)",
      (sum(lst)/len(lst))
     )
print('Максимальне значення:', max(lst))
print('Мінімальне значення:', min(lst))
odd = [num for num in lst if num % 2 == 1]
print('Кількість парних чисел:', len(lst)-len(odd))
print('Кількість непарних чисел:', len(odd))