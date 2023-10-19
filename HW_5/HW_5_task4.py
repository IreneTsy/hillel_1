num = int(input("Write natural number: "))
for i in range(num):
    if i**2 <= num and i != 0:
        print(i**2, end=' ')