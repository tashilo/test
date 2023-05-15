def sanitize_file(source, output):
    # Используя менеджер контекста для чтения файла source
    with open(source, 'r') as source_file:
        # Чтение содержимого файла
        content = source_file.read()

        # Очистка содержимого файла от цифр
        sanitized_content = ''.join(char for char in content if not char.isdigit())

    # Используя менеджер контекста для записи файла output
    with open(output, 'w') as output_file:
        # Запись очищенного содержимого в файл output
        output_file.write(sanitized_content)

source = "6. модуль - работа с файлами\\source.txt"
output = "6. модуль - работа с файлами\\output.txt"
sanitize_file(source, output)