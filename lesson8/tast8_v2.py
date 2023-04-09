import os

from model_test import create_record, filter_records_surname, export_in_file, read_file, change_records, delete_records
from view_test import file_path, menu_buttons, view_notion, show_list_tuple_dict, show_list_dict, create_new_file, \
    user_request


# Меню программы
def menu(data_phonebook):
    while True:
        user_input = menu_buttons()

        # Вывести словарь на экран
        if user_input == "о":
            if len(data_phonebook) == 0:
                view_notion("данные не найдены", "x", "x")
            else:
                show_list_dict(data_phonebook)
        # Новая запись
        if user_input == "н":
            if len(data_phonebook) != 0:
                create_record(data_phonebook)
                view_notion("новая запись", separator_end="—")
            else:
                view_notion("ошибка импорта", "x", "x")
        # Вывести имеющиеся данные по фильтру 'Фамилия'
        if user_input == "ф":
            surname_filter = filter_records_surname(data_phonebook)
            if len(surname_filter) != 0:
                view_notion("результат поиска", "—", "—")
                show_list_tuple_dict(surname_filter)

            else:
                view_notion("пустой справочник")
        # Экспортировать данные в файл
        if user_input == "э":
            if len(data_phonebook) != 0:
                export_file_path = file_path()
                if path_check(export_file_path):
                    # Экспортируем файл(путь к файлу и импортированный список PB)
                    export_in_file(export_file_path, data_phonebook)
                    view_notion("экспорт", "–", "–")
                else:
                    choice = create_new_file(export_file_path)
                    if choice == "Д":
                        export_in_file(export_file_path, data_phonebook)
                        view_notion("экспорт", "–", "–")
            else:
                view_notion("ошибка экспорта", "–", "–")
        # Импортировать данные из файла
        if user_input == "и":
            import_file_path = file_path()
            # import_file_path = "data/data1.txt"
            if path_check(import_file_path):  # Проверка указанного пути
                # Чтение файла
                data_phonebook = read_file(import_file_path)
                view_notion("импорт", "–", "–")
            else:
                view_notion("ошибка пути", "–", "–")
        # Выход
        if user_input == "в":
            view_notion("конец программы")
            break
        # Изменить поля выбранной записи
        if user_input == "з":
            if len(data_phonebook) != 0:  # проверка длины
                # запрос на отображение словаря
                if user_request("вывод словаря").capitalize() == "Д":
                    show_list_dict(data_phonebook)  # показать словарь
                surname_filter = filter_records_surname(
                    data_phonebook)  # включаем поиск по фамилии
                # функция замены по фамилии
                change_records(data_phonebook, surname_filter)
            else:
                view_notion("пустой справочник")
                view_notion("ошибка импорта")
        # Удаление записи
        if user_input == "у":
            if len(data_phonebook) != 0:  # проверка длины
                # запрос на отображение словаря
                if user_request("вывод словаря").capitalize() == "Д":
                    show_list_dict(data_phonebook)  # показать словарь
                surname_filter = filter_records_surname(
                    data_phonebook)  # включаем поиск по фамилии
                delete_person = delete_records(data_phonebook, surname_filter)
                view_notion("удален"), show_list_tuple_dict(delete_person)
            else:
                view_notion("пустой справочник", "x")
                view_notion("ошибка импорта", separator_end="x")


# Проверка пути
def path_check(file_path: str) -> bool:
    if os.path.isfile(file_path):
        return True
    else:
        return False
