import random

"""2 га функція очікує один обовязковий парметр і це має бути
2 вимірний список симетричний"""
def create_matrix(n):
        matrix = [
          [random.randint(0, 200) for _ in range(n)]
            for __ in range(n)
        ]
        max_len = max(len(str(max(row)) if row else 0) for row in matrix)
        for row in matrix:
            formatted_row = [f'{val:^{max_len}}' for val in row]
            print(' '.join(formatted_row))

print(create_matrix(5))