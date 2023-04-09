from view_test import get_record, user_request, view_notion, show_list_tuple_dict


# Создание новой записи в справочнике
def create_record(data_phonebook: list):
    # Запрос у пользователя данных для добавления в справочник
    return data_phonebook.append(get_record())


# фильтр в справочнике по фамилии
def filter_records_surname(data_phonebook) -> list:
    surname_filter = user_request("запрос фамилии").capitalize()
    found_records = []
    for idx, person in enumerate(data_phonebook):
        # Startswith Помогает определить начинается ли строка с символов указанных в скобках. Возвращает True or False
        # get возвращает значение по введенному ключу
        if person.get("surname").startswith(surname_filter):
            found_records.append((idx, person))
    return found_records  # список, кортеж, словарь


# Изменение полей выбранной записи согласно фильтру по фамилии
def change_records(data_phonebook, surname_filter):
    if len(surname_filter) == 1:  # если в словаре одна запись
        # добавляем функцию get record и перезаписываем данные
        record_number = surname_filter[0][0]
        view_notion("введите данные")
        data_phonebook[record_number] = get_record()
    elif len(surname_filter) > 1:  # если обнаружено несколько людей с одинаковой фамилией
        show_list_tuple_dict(surname_filter)
        record_number = int(user_request("несколько совпадений")) - 1
        data_phonebook[record_number] = get_record()
    else:
        view_notion("человек не найден")


# Удаление полей выбранной записи согласно фильтру по фамилии
def delete_records(data_phonebook, surname_filter):
    if len(surname_filter) == 1:  # если в словаре одна запись
        data_phonebook.pop(surname_filter[0][0])
        return surname_filter
    elif len(surname_filter) > 1:  # если обнаружено несколько людей с одинаковой фамилией
        show_list_tuple_dict(surname_filter)
        record_number = int(user_request("несколько совпадений")) - 1
        data_phonebook.pop(record_number)
        return data_phonebook[surname_filter]
    else:
        view_notion("человек не найден")


# Экспорт файла
def export_in_file(export_file, data):
    # w - запись
    with open(export_file, "w", encoding='utf-8') as file:
        for el in data:  # перебор строк в файле + \n
            file.write(
                f"{el['surname']},{el['name']},{el['phone']},{el['description']}\n")


# импорт справочника из файла и добавление его в список для обработки (чтобы сохранить его в памяти)
def read_file(file_path: str) -> list:
    data = []
    # r тип операции - чтение
    with open(file_path, "r", encoding='utf-8') as file:
        for string in file:  # перебор строк в файле + \n
            # убираем перенос строки и делим по запятой
            new_list = string.strip().split(",")
            data.append({"surname": new_list[0], 'name': new_list[1],
                        'phone': new_list[2], 'description': new_list[3]})
    return data
