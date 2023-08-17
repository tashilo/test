from collections import UserDict
from functools import partial

class Field:
    def __init__(self, value, is_required=False, is_multiple=False):
        if is_required and not value:
            raise ValueError("Это поле является обязательным")
        self.value = value
        self.is_multiple = is_multiple

class Name(Field):
    def __init__(self, value):
        super().__init__(value, is_required=True)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit():
            raise ValueError("Телефон должен содержать только цифры")
        super().__init__(value, is_multiple=True)

class Record:
    def __init__(self, name, phones=None):
        self.name = Name(name)
        self.phones = phones if phones else []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)   

    def edit_phone(self,index, phone_number):
        if index < 0 or index >= len(self.phones):
            raise IndexError("Некорректный индекс")
        self.phones[index].value = phone_number  

    def remove_phone(self, phone_number):
        phone = Phone(phone_number)
        for index, phone in enumerate(self.phones):
            if phone.value == phone_number:
                self.phones.pop(index)
                break    

class AddressBook(UserDict):
    def add_record(self, name, record):
        self.data[name] = record

# Декоратор обработки ошибок
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except(KeyError, ValueError, IndexError, TypeError):
            return "An error occurred. Please check your input."

    return wrapper


# Функции обработчики команд

@input_error
def add_contact(contact_book, name, phone):
    record = Record(name, [Phone(phone)])
    contact_book.add_record(name, record)
    return f'телефонный номер {name} {phone} добавлен'

@input_error
def change_contact(contact_book, name, phone):
    record = contact_book.data[name]
    record.phones[0].value = phone
    return f'у контакта {name} изменен номер телефона'

@input_error
def phone(contact_book, name):
    return contact_book[name].phones[0].value

@input_error
def show(contact_book, arg):
    if arg == 'all':
        return '\n'.join([f'{rec.name.valuea}: {rec.phones[0].value}' for rec in contact_book.values()])
    else:
        return 'Unknown argument. Please try again.'

@input_error
def hello():
    return "How can I help you?"



def parse_input(user_input):
    command_parts = user_input.lower().strip().split(' ')
    command = command_parts[0]
    arguments = command_parts[1:] if len(command_parts) > 1 else []
    return command, arguments

def command_parser(command, contact_book, *args):
    сommands = {
        'add': partial(add_contact, contact_book),
        'change': partial(change_contact, contact_book),
        'phone': partial(phone, contact_book),
        'show': partial(show, contact_book),
        'hello': partial(hello)
    }
    if command not in сommands:
        return 'Unknown command. Please try again.'
    return сommands[command](*args)




def main():
    contact_book = AddressBook()
    print('Я бот-Ассистент. Работаю с книгой контактов. Чем я могу тебе помочь?')

    while True:
        user_input = input('>> ')
        if user_input in ['good bye', 'close', 'exit']:
            print('До свидания!')
            break

        command, arguments = parse_input(user_input)
        response = command_parser(command, contact_book, *arguments)
        print(response) 

if __name__ == "__main__":
    main()
  