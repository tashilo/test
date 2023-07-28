def write_employees_to_file(employee_list, path):
    # Открываем файл в режиме записи
    file = open(path, 'w')

    # Обходим список списков сотрудников
    for department in employee_list:
        # Записываем информацию о каждом сотруднике с новой строки
        for employee in department:
            file.write(employee + '\n')

    # Закрываем файл
    file.close()


# Тестовый список сотрудников по отделам
employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

# Путь к файлу
path = '6. модуль - работа с файлами\\employees.txt'

# Запись данных о сотрудниках в файл
write_employees_to_file(employee_list, path)


