import pickle
from typing import List, Optional


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: Optional[List[Person]] = None):
        self.filename = filename
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            return pickle.load(file)


# Пример использования
if __name__ == "__main__":
    contacts = [
        Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
        Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False),
    ]

    persons = Contacts("user_class.dat", contacts)
    persons.save_to_file()

    persons_from_file = persons.read_from_file()

    print(persons == persons_from_file)  # Должно быть False
    print(
        persons.contacts[0].name == persons_from_file.contacts[0].name
    )  # Должно быть True
    print(
        persons.contacts[0].email == persons_from_file.contacts[0].email
    )  # Должно быть True
    print(
        persons.contacts[0].phone == persons_from_file.contacts[0].phone
    )  # Должно быть True
