#1. Наведено список чисел. Визначте, скільки у ньому зустрічається різних чисел.
#приклад: якщо в списку число 8 зустрічається 3 рази то це означає що в списку зустрічається 8мка.

lst = [2, 4, 3, 5, 6, 7, 3, 5, 9, 5, 6, 9]
lst_set = set(lst)
print(lst_set)
print('Кількість різних чисел в списку: ', len(lst_set))