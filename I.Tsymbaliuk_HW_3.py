#1.
n = int(input('Кількість школярів: '))
k = int(input('Кількість яблук: '))
q_ty = k//n
left = k%n
print('Кожному школяру дісталося яблук:', q_ty)
print('Яблук залишилось в корзинці:', left)

#2.
a = int(input('Клас А:'))
b = int(input('Клас Б:'))
c = int(input('Клас В:'))
print('Кількість парт що треба закупити :', -((a//-2)+(b//-2)+(c//-2)))

#3.
p = int(input('Введіть пароль: '))
saved_pass = (12345, 56789, 34567)
if p in saved_pass:
    print('Пароль прийнято!')
else:
    print('Вам відмовлено в доступі!')

#4.
year = int(input('Рік: '))
if year > 1900 and year < 1_000_000:
    if bool(year%4) == False and bool(year%100) == False and bool(year%400) == False:
        print(year, 'is a leap year')
    else:
        print(year, 'is not a leap year')

else:
    print('Year does not meet demands!')