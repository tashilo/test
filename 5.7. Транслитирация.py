# задаем кириллические символы и их соответствие в латинской транслитерации
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "e",
    "j",
    "z",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "",
    "y",
    "",
    "e",
    "yu",
    "ya",
    "je",
    "i",
    "ji",
    "g",
)

# создаем словарь транслитерации
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


# создаем функцию translate, которая транслитерирует строку из кириллицы в латиницу
def translate(name):
    lat_name = ""
    for cyr_simv in name:
        # проверяем, что символ есть в словаре транслитерации
        if ord(cyr_simv) in TRANS:
            # добавляем соответствующий латинский символ
            lat_name = lat_name + TRANS[ord(cyr_simv)]
        else:
            # если символ не требует транслитерации, добавляем его в исходном виде
            lat_name = lat_name + cyr_simv

    return lat_name


# тестируем функцию translate
print(translate("Дмитрий Коробов"))  # Dmitrij Korobov
print(translate("Александр Иванович"))  # Aleksandr Ivanovich
