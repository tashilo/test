# 9.9 Отфильтровать положительные значения

def positive_values(list_payment):
    return list(filter(lambda x: x > 0, list_payment))

payment = [100, -3, 400, 35, -100]
positive_payments = positive_values(payment)
print(positive_payments)  # Вывод: [100, 400, 35]


#9.10 Отфильтровать избраные контакты

def get_favorites(contacts):
    return list(filter(lambda contact: contact["favorite"], contacts))

contacts = [
    {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
    {"name": "Jane Smith", "email": "jane@example.com", "phone": "(123) 456-7890", "favorite": True},
    {"name": "John Doe", "email": "john.doe@example.com", "phone": "(987) 654-3210", "favorite": True},
]

favorites = get_favorites(contacts)
for contact in favorites:
    print(contact["name"])  # Выводит имена избранных контактов