a = int(input("Write natural number: "))

for n in range(a):
    square = n*n
    lst_n = list(str(n))
    lst_sq = list(str(square))
    len_n = len(lst_n)
    len_sq = len(lst_sq)
    if lst_n[::] == lst_sq[(len_sq-len_n):len_sq] and n > 0:
        print(n, "*", n, "=", n*n)