def format_phone_number(func):
    def wrapper(phone):
        result = func(phone)
        if len(result) == 10:
            return '+38' + result
        elif len(result) == 12:
            return '+' + result
        else:
            return result
    return wrapper    
    


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

# Test

phones = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

for phone in phones:
    print(sanitize_phone_number(phone))