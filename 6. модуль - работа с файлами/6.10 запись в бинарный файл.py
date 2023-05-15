def save_credentials_users(path, users_info):
    with open(path, "wb") as file:
        for username, password in users_info.items():
            line = f"{username}:{password}\n".encode("utf-8")
            file.write(line)

path = "6. модуль - работа с файлами\\users_credentials.bin"
users_info = {
    'andry': 'uyro18890D',
    'steve': 'oppjM13LL9e',
}

save_credentials_users(path, users_info)


