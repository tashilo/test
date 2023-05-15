import base64

def get_credentials_users(path):
    with open(path, "rb") as file:
        # декодируем байты файла в строки, используя utf-8 кодировку
        lines = [line.decode("utf-8").strip() for line in file.readlines()]
        return lines

path = "6. модуль - работа с файлами\\users_credentials.bin"
print(get_credentials_users(path))

data = get_credentials_users(path)



def encode_data_to_base64(data):
    encoded_data = []
    for item in data:
        encoded_item = base64.b64encode(item.encode('utf-8')).decode('utf-8')
        encoded_data.append(encoded_item)
    return encoded_data


print(encode_data_to_base64(data))
    