import csv


# Функция для записи контактов в файл
def write_contacts_to_file(filename, contacts):
    # Открываем файл для записи
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        # Создаем объект writer и указываем заголовки столбцов
        fieldnames = ["name", "email", "phone", "favorite"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Записываем заголовки и данные в файл
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


# Функция для чтения контактов из файла
def read_contacts_from_file(filename):
    contacts = []
    # Открываем файл для чтения
    with open(filename, "r", encoding="utf-8") as csvfile:
        # Создаем объект reader
        reader = csv.DictReader(csvfile)

        # Читаем и преобразуем каждую строку
        for row in reader:
            # Преобразуем значение favorite к типу bool
            row["favorite"] = row["favorite"] == "True"
            contacts.append(row)
    return contacts


# Пример использования
if __name__ == "__main__":
    contacts = [
        {
            "name": "Allen Raymond",
            "email": "nulla.ante@vestibul.co.uk",
            "phone": "(992) 914-3792",
            "favorite": False,
        },
        {
            "name": "Chaim Lewis",
            "email": "dui.in@egetlacus.ca",
            "phone": "(294) 840-6685",
            "favorite": False,
        },
        # ... и так далее
    ]

    write_contacts_to_file("contacts.csv", contacts)

    read_contacts = read_contacts_from_file("contacts.csv")
    print(read_contacts)
