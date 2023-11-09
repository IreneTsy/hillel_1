def longest_words(file):
    # Створюємо функцію, яка буде отримувати файл на вхід та вичитувати дані
    # відображати найдовже число, як результат

    # Створюємо список, який буде отримувати текст у вигляді списку построчно
    lst =[]

    with open(file, 'r') as handler:
        # Відкриваємо текстовий файл на читання та перебираємо текст построчно
        for line in handler:
            # Заміна абзаців на пробіл
            chng_line = line.replace('\n', ' ')
            # Розділяємо строку на окремі елементи списку
            chng_line = chng_line.split(' ')
            # Додаємо до основного списку в циклі
            lst = lst + chng_line

# Створюємо словник
    new_dct = {}
    for i in lst:
        # Всі елементи списку перетворюємо в елементи словника,
        # де ключем буде слово, а значенням - його довжина
        new_dct.setdefault(i, len(i) - 1)
        new_dct[i] += 1
    del new_dct[''] # Видаляєио пусті значення зі словника

# Визначаємо найдовше слово в словнику
    print(max(new_dct, key=new_dct.get))
    handler.close()

result = longest_words('article.txt')
print(result)