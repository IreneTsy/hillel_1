import random
import pprint


def sort_matrix(M):
    # Створення двовимірного списку МхМ
    matrix = [
        [random.randint(1, 50) for _ in range(M)]
        for _ in range(M)
    ]
    print(f"Двовимірний список розмірами {M}х{M} до сортування")
    pprint.pprint(matrix)
    print()
    print()

    # Сортування стовпців матриці за сумою їх елементів
    # Створюємо список для сум стовпців
    column_sums = [sum(row[i] for row in matrix) for i in range(M)]

    # Виконуємо сортування за сумами стовпців
    for i in range(M - 1):
        for j in range(0, M - i - 1):
            if column_sums[j] > column_sums[j + 1]:
                # Міняємо місцями суми
                column_sums[j], column_sums[j + 1] =\
                    (column_sums[j + 1], column_sums[j])
                # Міняємо місцями стовпці
                for row in matrix:
                    row[j], row[j + 1] = row[j + 1], row[j]
                    #print(row)

    # Сортування елементів у стовпцях
    for j in range(M):
        # Для непарних стовпців сортуємо знизу вгору
        if j % 2:
            for i in range(M - 1):
                for k in range(0, M - i - 1):
                    if matrix[k][j] < matrix[k + 1][j]:
                        matrix[k][j], matrix[k + 1][j] = \
                        (matrix[k + 1][j], matrix[k][j])
        # Для парних стовпців - зверху донизу
        else:
            for i in range(M - 1, 0, -1):
                for k in range(M - 1, M - i - 1, -1):
                    if matrix[k][j] < matrix[k - 1][j]:
                        matrix[k][j], matrix[k - 1][j] =\
                        matrix[k - 1][j], matrix[k][j]

    return matrix, column_sums


def print_matrix(matrix, column_sums):
    # Виведення матриці
    for row in matrix:
        for elem in row:
            print(f"{elem:3d}", end=" ")
        print()

    # Виведення сум
    for s in column_sums:
        print(f"{s:3d}", end=" ")
    print()


# Введення розміру матриці
if __name__ == "__main__":
    M = int(input("Введіть число > 5: "))
    if M <= 5:
        print("Число має бути більше 5")
    else:
        sorted_matrix, column_sums = sort_matrix(M)
        print('Відсортований двовимірний список')
        print_matrix(sorted_matrix, column_sums)