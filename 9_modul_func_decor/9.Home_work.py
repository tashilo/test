from functools import partial
# Обработка ошибок и неверного ввода - ДЕКОРАТОР
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except(KeyError, ValueError, IndexError, TypeError):
            return "An error occurred. Please check your input."

    return wrapper


# Парсер команд. 
# Часть, которая отвечает за разбор введенных пользователем строк, выделение из строки ключевых слов и модификаторов команд.
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

def parse_input(user_input):
    command_parts = user_input.lower().strip().split(' ')
    command = command_parts[0]
    arguments = command_parts[1:] if len(command_parts) > 1 else []
    return command, arguments

# Функции обработчики команд — набор функций, которые ещё называют handler, они отвечают за непосредственное выполнение команд.
# добавление, изменение, поиск, вывод всех контактов
@input_error
def add_contact(contact_book, name, phone):
    contact_book[name] = phone
    return f'телефонный номер {name} {phone} добавлен'

@input_error
def change_contact(contact_book, name, phone):
    contact_book[name] = phone
    return f'у контакта {name} изменен номер телефона'

@input_error
def phone(contact_book, name):
    return contact_book[name]

@input_error
def show(contact_book, arg):
    if arg == 'all':
        return '\n'.join(map(lambda x: f'{x[0]}: {x[1]}', contact_book.items()))
    else:
        return 'Unknown argument. Please try again.'

@input_error
def hello():
    return "How can I help you?"


# Цикл запрос-ответ. Эта часть приложения отвечает за получение от пользователя данных и возврат пользователю ответа от функции-handlerа.

def main():
    contact_book = {}
    print('Я бот-Ассистент. Работаю с книгой контактов. Чем я могу тебе помочь?')

    while True:
        user_input = input('>> ')
        if user_input in ['good bye', 'close', 'exit']:
            print('До свидания!')
            break

        command, arguments = parse_input(user_input)
        response = command_parser(command, contact_book, *arguments)
        print(response) 

main()
  