import random
import pprint
n = int(input('Input number'))
matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
pprint.pprint(matrix)

print('Сума чисел по діагоналі:',
    sum([matrix[i][i] for i in range(n)])
)

print('Сума чисел останнього стовбця:',
    sum([matrix[i][n-1] for i in range(n)])
)