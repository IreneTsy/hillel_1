n = int(input('Input number: '))
n_1 = n
for n in range(n):
    my_string = '1' + ('0' * n)
    print(("%.0f"%(n)).rjust(2), my_string.rjust(n_1))