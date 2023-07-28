def total_salary(path):
    total = 0.0  # Инициализация общей суммы зарплаты

    # Открыть файл с помощью функции open()
    fh = open(path, 'r')

    # Чтение файла построчно
    line = fh.readline()
    while line:
        # Разделить строку на имя разработчика и зарплату
        name, salary = line.strip().split(',')

        # Добавить зарплату к общей сумме
        total = total + float(salary)

        # Чтение следующей строки
        line = fh.readline()

    # Закрыть файл
    fh.close()

    return total

# Пример использования функции
path = "6. модуль - работа с файлами\\salaries.txt"  # Укажите здесь путь к вашему файлу
print("Общая сумма зарплат всех разработчиков:", total_salary(path))

