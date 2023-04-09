# Путь к файлу
def file_path() -> str:
    return input("\nУкажите путь к файлу (пример: data/data1.txt): ")


# Запрос новых данных в словарь
def get_record():
    return {"surname": input("Введите фамилию: ").capitalize(),
            "name": input("Введите имя: ").capitalize(),
            "phone": input("Введите телефон: "),
            "description": input("Введите описание: ").capitalize()}


# Отображение меню
def menu_buttons() -> str:
    print("\nГлавное меню",
          "—" * 35,
          "(н)Новая запись",
          "(у)Удалить запись",
          "(з)Заменить запись",
          "(о)Отобразить словарь на экране",
          "(ф)Фильтр по 'Фамилии'",
          "(и)Импортировать данные из файла",
          "(э)Экспортировать данные в файл",
          "(в)Выход",
          "—" * 35, sep="\n")

    return input("Введите нужную букву -> ").lower()


# Отображение лист_кортеж_словарь
def show_list_tuple_dict(data_phonebook: list):
    if data_phonebook:
        for key, record in data_phonebook:
            print(f"№{key + 1}. Фамилия: {record['surname']}, Имя: {record['name']}, Телефон: {record['phone']}, "
                  f"Описание: {record['description']}")


# отображение список_словарь
def show_list_dict(data_phonebook: list):
    if data_phonebook:
        for idx, record in enumerate(data_phonebook):
            print(f"№{idx + 1}. Фамилия: {record['surname']}, Имя: {record['name']}, Телефон: {record['phone']}, "
                  f"Описание: {record['description']}")


# Показать уведомление
def view_notion(choice_notion, separator_start="", separator_end=""):
    notion = {"": "",
              "новая запись": "Новая запись создана в словаре.",
              "пустой справочник": "Ваш телефонный справочник пуст.",
              "ошибка импорта": "Сначала вам нужно импортировать телефонный справочник!",
              "ошибка экспорта": "Нечего экспортировать. Ваш файл пуст. Проверьте файл импорта.",
              "ошибка пути": "Путь к файлу указан неправильно",
              "результат поиска": "Результат поиска:",
              "данные не найдены": "Данные не найдены, возможно вы не импортировали файл.",
              "экспорт": "Файл экспортирован в указанном пути.",
              "импорт": "Файл успешно импортирован.",
              "файл не найден": "Файл не найден.",
              "конец программы": "Конец программы",
              "человек не найден": "Человек в справочнике не найден",
              "введите данные": "Введите новые данные:",
              "удален": "В словаре удалена следующая запись:",
              "меню": "Главное меню:"}
    if separator_start:
        separator_start = separator_start * len(notion[choice_notion]) + "\n"
    if separator_end:
        separator_end = "\n" + separator_end * len(notion[choice_notion])

    return print(f"{separator_start}{notion[choice_notion]}{separator_end}")


# Вопрос создания нового файла
def create_new_file(export_file_path: str) -> str:
    view_notion("файл не найден")
    return input(f"Создать eго в указанном пути? <{export_file_path}> Д-да, если нет нажмите 'Enter': ").upper()


# Все запросы пользователю
def user_request(choice_notion: str) -> str:
    request = {"вывод словаря": "Вывести словарь на экран? 'Д-Да' если нет, нажмите 'Enter'",
               "создать файл": "создать новый файл в директории?",
               "запрос фамилии": "Введите фамилию для поиска пользователя",
               "несколько совпадений": "Найдено несколько позиций удовлетворяющих фильтру.\nУкажите номер нужного "
                                       "человека: "}
    return input(request[choice_notion])

# def ask_surname(default_value: str = ""):
#     return input(f"Введите фамилию {f'({default_value})' if default_value else ''} > ") or default_value
