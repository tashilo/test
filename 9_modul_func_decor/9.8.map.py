def get_emails(list_contacts):
    return list(map(lambda contact: contact["email"], list_contacts))

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "John Smith",
        "email": "john.smith@example.com",
        "phone": "(123) 456-7890",
        "favorite": True,
    },
]

emails = get_emails(contacts)
print(emails)  # Вывод: ['nulla.ante@vestibul.co.uk', 'john.smith@example.com']
