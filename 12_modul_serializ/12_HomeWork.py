from collections import UserDict
from datetime import datetime
from functools import partial
import pickle


# Класс Field, который родительский для всех полей. По умолчанию передает параметр, что поле необязательное.
class Field:
    def __init__(self, value, is_required=False):
        if is_required and not value:
            raise ValueError("Это поле является обязательным")
        self.value = value


class Name(Field):
    def __init__(self, value):
        super().__init__(value, is_required=True)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not self.validate_phone(new_value):
            raise ValueError(
                "Некоректний номер телефоную. Код должен состоять из 13-ти знаков и начинаться с кода страны. Например: +381234567890"
            )
        self._value = new_value

    def validate_phone(self, value):
        return value.startswith("+380") and len(value) == 13 and value[1:].isdigit()


# Клас для дня народження
class Birthday(Field):
    def __init__(self, value=None):
        if value and not self.validate_birthday(value):
            raise ValueError("Некоректна дата народження")
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not self.validate_birthday(new_value):
            raise ValueError("Некоректна дата народження")
        self._value = new_value

    def validate_birthday(self, value):
        try:
            date = datetime.strptime(value, "%Y-%m-%d")
            # Перевірка чи дата не в майбутньому
            if date > datetime.now():
                return False
        except ValueError:
            return False
        return True


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phone = []
        if phone:
            self.add_phone(phone)
        self.birthday = Birthday(birthday)

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phone.append(phone)

    def edit_phone(self, index, phone_number):
        if index < 0 or index >= len(self.phone):
            raise IndexError("Некорректный индекс")
        self.phone[index].value = phone_number

    def remove_phone(self, phone_number):
        target_phone = Phone(phone_number)
        for index, existing_phone in enumerate(self.phone):
            if existing_phone.value == target_phone.value:
                self.phone.pop(index)
                break

    def days_to_birthday(self):
        if not self.birthday.value:
            return None
        birth_date = datetime.strptime(self.birthday.value, "%Y-%m-%d")
        today = datetime.now()
        next_birthday = birth_date.replace(year=today.year)
        if today > next_birthday:
            next_birthday = next_birthday.replace(year=today.year + 1)
        delta = next_birthday - today
        return delta.days


class AddressBook(UserDict):
    def __init__(self, records_per_page=5):
        super().__init__()
        self.records_per_page = records_per_page

    def add_record(self, name, record):
        self.data[name] = record

    def iterator(self, page=1):
        start_index = (page - 1) * self.records_per_page
        end_index = start_index + self.records_per_page
        items = list(self.data.items())[start_index:end_index]
        for item in items:
            yield item

    # Сохраняем в файл
    def save_to_file(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.data, f)

    # Загружаем из файла
    def load_from_file(self, filename):
        with open(filename, "rb") as f:
            self.data = pickle.load(f)

    # Поиск по адресной книге
    def search(self, query):
        results = {}
        for name, record in self.data.items():
            if query.lower() in name.lower():
                results[name] = record
            else:
                for phone in record.phone:
                    if query in phone.value:
                        results[name] = record
                        break
        return results


# Декоратор обработки ошибок
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return str(error)  # Возврат текста ошибки ValueError
        except (KeyError, IndexError, TypeError):
            return "An error occurred. Please check your input."

    return wrapper


# Функции обработчики команд


@input_error
def add_contact(contact_book, name, phone):
    record = Record(name, phone)
    contact_book.add_record(name, record)
    return f"телефонный номер {name} {phone} добавлен"


@input_error
def change_contact(contact_book, name, phone):
    record = contact_book.data[name]
    record.phone.value = phone
    return f"у контакта {name} изменен номер телефона"


@input_error
def phone(contact_book, name):
    return contact_book[name].phone.value


@input_error
def show(contact_book, arg):
    if arg == "all":
        return "\n".join(
            [
                f"{rec.name.value}: {rec.phone.value}"
                for rec in contact_book.values()
                if rec.phone
            ]
        )
    else:
        return "Unknown argument. Please try again."


@input_error
def search_contact(contact_book, query):
    found = contact_book.search(query)
    if found:
        return "\n".join(
            [
                f"{name}: {', '.join([p.value for p in rec.phone])}"
                for name, rec in found.items()
            ]
        )
    else:
        return "Контакт не найден"


def save_to_file(contact_book, filename):
    contact_book.save_to_file(filename)
    return "Адресная книга сохранена."


def load_from_file(contact_book, filename):
    try:
        contact_book.load_from_file(filename)
        return "Адресная книга загружена."
    except FileNotFoundError:
        return "Файл не найден."


@input_error
def hello():
    return "How can I help you?"


def parse_input(user_input):
    command_parts = user_input.lower().strip().split(" ")
    command = command_parts[0]
    arguments = command_parts[1:] if len(command_parts) > 1 else []
    return command, arguments


def command_parser(command, contact_book, *args):
    сommands = {
        "add": partial(add_contact, contact_book),
        "change": partial(change_contact, contact_book),
        "phone": partial(phone, contact_book),
        "show": partial(show, contact_book),
        "hello": partial(hello),
        "search": partial(search_contact, contact_book),  # новая команда
        "save": partial(
            save_to_file, contact_book, "address_book.pkl"
        ),  # новая команда
        "load": partial(
            load_from_file, contact_book, "address_book.pkl"
        ),  # новая команда
    }
    if command not in сommands:
        return "Unknown command. Please try again."
    return сommands[command](*args)


def main():
    contact_book = AddressBook()
    print("Я бот-Ассистент. Работаю с книгой контактов. Чем я могу тебе помочь?")

    while True:
        user_input = input(">> ")
        if user_input in ["good bye", "close", "exit"]:
            print("До свидания!")
            break

        command, arguments = parse_input(user_input)
        response = command_parser(command, contact_book, *arguments)
        print(response)


if __name__ == "__main__":
    main()
