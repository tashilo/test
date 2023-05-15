def add_employee_to_file(record, path):
    # Открываем файл в режиме добавления
    file = open(path, 'a')

    # Записываем сотрудника в файл, начиная с новой строки
    file.write(record + '\n')

    # Закрываем файл
    file.close()


# Путь к файлу
path = '6. модуль - работа с файлами\\employees.txt'

# Добавление нового сотрудника в файл
new_employee = 'Drake Mikelsson, 19'
add_employee_to_file(new_employee, path)

