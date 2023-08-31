import pickle


# Функция для записи контактов в файл
def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as f:  # Открываем файл на запись в бинарном режиме
        pickle.dump(contacts, f)  # Сохраняем список контактов в файл


# Функция для чтения контактов из файла
def read_contacts_from_file(filename):
    with open(filename, "rb") as f:  # Открываем файл на чтение в бинарном режиме
        contacts = pickle.load(f)  # Загружаем список контактов из файла
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

    write_contacts_to_file("contacts.pkl", contacts)

    read_contacts = read_contacts_from_file("contacts.pkl")
    print(read_contacts)
