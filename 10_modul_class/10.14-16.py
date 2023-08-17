class Contacts:
    current_id = 1  # переменная класса для уникального идентификатора контакта

    def __init__(self):
        self.contacts = []  # переменная экземпляра для хранения контактов

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        # Создание словаря контакта с уникальным идентификатором
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }
        self.contacts.append(contact)  # добавление контакта в список
        Contacts.current_id += 1  # увеличение идентификатора на 1
    
    def get_contact_by_id(self, id):
        # Поиск контакта по id в списке контактов
        for contact in self.contacts:
            if contact["id"] == id:
                return contact
        return None  # Возврат None, если контакт не найден

    def remove_contacts(self, id):
        # Поиск контакта по id в списке контактов
        for contact in self.contacts:
            if contact["id"] == id:
                self.contacts.remove(contact)  # Удаление контакта из списка
                break  # Выход из цикла после удаления