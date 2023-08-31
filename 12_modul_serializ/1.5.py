import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts
        self.count_save = 0

    def __getstate__(self):
        state = self.__dict__.copy()
        state["count_save"] = self.count_save + 1
        return state

    def save_to_file(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self, f)

    def read_from_file(self):
        with open(self.filename, "rb") as f:
            return pickle.load(f)


# Пример использования
contacts = [
    Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
    Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()

first = persons.read_from_file()
first.save_to_file()

second = first.read_from_file()
second.save_to_file()

third = second.read_from_file()

print(persons.count_save)  # должно вывести 0
print(first.count_save)  # должно вывести 1
print(second.count_save)  # должно вывести 2
print(third.count_save)  # должно вывести 3
