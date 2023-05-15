list_phones = [    
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "81050-111-22-22",
    "65050 111 22 11   ",
    ]

def sanitize_phone_number(list_phones):
    list = []
    for phone in list_phones:
        new_phone = (phone.strip()
                    .removeprefix("+")
                    .replace("(", "")
                    .replace(")", "")
                    .replace("-", "")
                    .replace(" ", ""))
        if new_phone.startswith("38") == False:
            new_phone = "38" + new_phone  
        list.append(new_phone)
    result =  '\n'.join(list) 

    return result

print(sanitize_phone_number(list_phones))

