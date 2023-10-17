a = input()
if len(a) > 0:
    while len(a) < 15:
        a *= 3        
        #print(a)
    if len(a) >= 15:
        a = list(a)
        print('Повний список', a, sep='\n')
        print('Остaнні 5 елементів зі списку', a[(len(a)-5):len(a):1], sep='\n')
        print('Дзеркально обернений список', a[::-1], sep='\n')
        print('Список усіх парних елементів', a[1::2], sep='\n')
        print('Cписок у якому 5 елементів спочатку такі ж самі як остані 5 елементів списку', a[(len(a)-5):len(a):1] + a[5::], sep='\n')
else:
    print("End")
	
first = (1,2,3)
second = (3,4,5)
result = list(first)
#print(second)
result.extend(second)
print('Завдання 2', 'A)', result, sep='\n')
t_result = (result, first[::-1], second[::-1])
print('B)', t_result, sep='\n')
print('C)' ,t_result[0][2], t_result[1][2], t_result[2][2], sep='\n')