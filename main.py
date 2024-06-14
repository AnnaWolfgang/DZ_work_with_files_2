def work_with_phonebook():
    phone_book = read_txt('phon.txt')

    while True:
        choice = show_menu()

        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            result = change_number(phone_book, last_name, new_number)
            if result:
                write_txt('phon.txt', phone_book)
            print(result)
        elif choice == 4:
            last_name = input('Введите фамилию: ')
            result = delete_by_lastname(phone_book, last_name)
            if result == "Абонент удален.":
                write_txt('phon.txt', phone_book)
            print(result)
        elif choice == 5:
            number = input('Введите номер: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('Введите новые данные (Формат: Фамилия, Имя, Номер, Описание): ')
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)
            print("Абонент добавлен.")
        elif choice == 7:
            source_file = input('Введите имя исходного файла: ')
            destination_file = input('Введите имя файла назначения: ')
            line_number = int(input('Введите номер строки для копирования: '))
            copy_line(source_file, destination_file, line_number)
        elif choice == 8:
            write_txt('phon.txt', phone_book)
            print("Работа завершена.")
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер абонента\n"
          "4. Удалить абонента по фамилии\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить абонента в справочник\n"
          "7. Копировать данные из одного файла в другой\n"
          "8. Закончить работу")
    choice = int(input("Введите номер действия: "))
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)

    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

def print_result(phone_book):
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book, last_name):
    result = [record for record in phone_book if record['Фамилия'] == last_name]
    return result if result else "Абонент не найден."

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return "Номер изменен."
    return "Абонент не найден."

def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            phone_book.remove(record)
            return "Абонент удален."
    return "Абонент не найден."

def find_by_number(phone_book, number):
    result = [record for record in phone_book if record['Телефон'] == number]
    return result if result else "Абонент не найден."

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)
    return "Абонент добавлен."

def copy_line(source_file, destination_file, line_number):
    try:
        with open(source_file, 'r', encoding='utf-8') as src, open(destination_file, 'a', encoding='utf-8') as dst:
            lines = src.readlines()
            if line_number - 1 < len(lines):
                dst.write(lines[line_number - 1])
                print("Строка скопирована успешно.")
            else:
                print("Номер строки вне диапазона.")
    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что имя файла указано правильно и файл существует.")

work_with_phonebook()