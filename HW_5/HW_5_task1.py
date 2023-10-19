num = input('Введіть число ', )
n = list(num)

for i, l in enumerate(n):
        print(i, l, n[(i+1):])
        if l in n[(i+1):] :
            print('Так')
            break
#        i = i+1
else:
    print('Ні')