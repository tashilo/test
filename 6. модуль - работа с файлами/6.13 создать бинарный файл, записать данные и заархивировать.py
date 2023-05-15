import shutil

def create_backup(path, file_name, employee_residence):
    # Создаем бинарный файл и записываем информацию из словаря employee_residence
    full_path = f"{path}/{file_name}"
    with open(full_path, "wb") as file:
        for name, country in employee_residence.items():
            line = f"{name} {country}\n".encode("utf-8")
            file.write(line)
    
    # Архивируем папку по пути path
    archive_name = "backup_folder"
    shutil.make_archive(archive_name, "zip", path)

    return f"{path}/{archive_name}.zip"

# Пример использования функции
path = "6. модуль - работа с файлами"
file_name = "employee_residence.bin"
employee_residence = {
    'Michael': 'Canada',
    'John': 'USA',
    'Liza': 'Australia'
}

print(create_backup(path, file_name, employee_residence))
