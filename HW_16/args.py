import argparse


# python args.py --file file_to_read.txt

def usage():
    parser = argparse.ArgumentParser(
       description="Parse file and demo information.",
       #epilog="Designed by developer Iryna Tsymbaliuk",
       prog="args"
    )

    parser.add_argument(
       '-f', '--file',
       required=True,  # обовязковый параметр для вводу
       type=str,  # тип даних
       help='Повний або відносний шлях до файлу'  # пояснення для опцій
     )

    parser.add_argument(
       'filename',
        type=argparse.FileType('r'),
        help='Повний або відносний шлях до файлу'  # пояснення для опцій
    )

    args = parser.parse_args()

    with open(args.filename) as handler:
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
    del new_dct['']  # Видаляєио пусті значення зі словника

    # Визначаємо найдовше слово в словнику
    print(max(new_dct, key=new_dct.get))
#

def main():
    arguments = usage()
    print("arguments.file: ", arguments.file)


if __name__ == "__main__":
    main()

