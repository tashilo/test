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
        self.is_unpacking = False  # новый атрибут

    def __getstate__(self):
        state = self.__dict__.copy()
        state["count_save"] = self.count_save + 1
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.is_unpacking = True  # изменяем значение при распаковке

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
person_from_file = persons.read_from_file()

print(persons.is_unpacking)  # должно вывести False
print(person_from_file.is_unpacking)  # должно вывести True
