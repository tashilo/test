import json


# Функция для записи контактов в файл
def write_contacts_to_file(filename, contacts):
    with open(filename, "w", encoding="utf-8") as f:  # Открываем файл на запись
        json_data = {
            "contacts": contacts
        }  # Создаем словарь с ключом "contacts" и вашим списком контактов
        json.dump(
            json_data, f, ensure_ascii=False, indent=4
        )  # Сохраняем JSON-структуру в файл


# Функция для чтения контактов из файла
def read_contacts_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:  # Открываем файл на чтение
        json_data = json.load(f)  # Читаем JSON-структуру из файла
        contacts = json_data.get(
            "contacts", []
        )  # Получаем список контактов по ключу "contacts"
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
            "name": "Tanya",
            "email": "tanya@example.com",
            "phone": "+380631234567",
            "favorite": True,
        },
    ]

    write_contacts_to_file("contacts.json", contacts)

    read_contacts = read_contacts_from_file("contacts.json")
    print(read_contacts)
