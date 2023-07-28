def save_applicant_data(source, output):
    # Преобразуем список словарей в список строк
    lines = []
    for applicant in source:
        line = f"{applicant['name']},{applicant['specialty']},{applicant['math']},{applicant['lang']},{applicant['eng']}\n"
        lines.append(line)

    # Записываем данные в файл
    with open(output, "w") as file:
        file.writelines(lines)

# Пример использования функции:
applicants = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

save_applicant_data(applicants, "6. модуль - работа с файлами\\output.txt")





