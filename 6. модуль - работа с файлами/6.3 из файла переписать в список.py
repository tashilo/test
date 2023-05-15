def read_employees_from_file(path):
    # Открываем файл в режиме чтения
    file = open(path, 'r')

    # Создаем пустой список сотрудников
    employees = []

    # Читаем строки из файла и добавляем их в список сотрудников
    for line in file:
        # Удаляем символ конца строки и добавляем строку в список сотрудников
        employees.append(line.strip())

    # Закрываем файл
    file.close()

    # Возвращаем список сотрудников
    return employees


# Путь к файлу
path = '6. модуль - работа с файлами\\employees.txt'

# Чтение данных о сотрудниках из файла
employees = read_employees_from_file(path)

# Вывод списка сотрудников
print(employees)

