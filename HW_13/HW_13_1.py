# Cпочатку створюємо та відкриваємо файл на запис
with open('text_file','w') as handler:

while True:
    # Якщо умова виконується, тоді просимо ввести значення
    n = input('New note: ')
    handler.write(f'{n}\n') # Записуємо отриманні введені дані в файл
    if len(n) == 0: # Ввод зупиняється якщо строка пуста
        break

# Pакриваємо файл
handler.close()