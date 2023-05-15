import os
import re
import shutil
import sys
from typing import Tuple

# Функция принимает имя файла и приводит его к латинской транслитерации с сохранением разряда.
# Кирилические буквы переводит, латинские буквы и цифры оставляет как есть, остальные символы заменяет на "_"
def normalize(name: str) -> str:
    # Словарь соответствия кириллических символов латинским
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',
        'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
        'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya'
    }
    result = []
    for simv in name:
        if re.match(r'[a-zA-Z0-9]', simv):
            result.append(simv)
        elif re.match(r'[а-яА-Я]', simv):
            if simv in translit_dict:
                result.append(translit_dict[simv])
            else:
                simv = simv.lower()
                result.append(translit_dict[simv])
        else:
            result.append('_')
    return ''.join(result)  



# Функция определения категорий файлов в зависимости от расширения файла (extension).
# Если раширение файла (в верхнем регистре) совпадает со значениями словаря categories,/
#  тогда функция возвращает соответствующую категорию из ключей словаря. 
# Если не совпадает - возвращает 'unknown'
def categorize(extension: str) -> str:
    categories = {
        'images': ('JPEG', 'PNG', 'JPG', 'SVG'),
        'video': ('AVI', 'MP4', 'MOV', 'MKV'),
        'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
        'audio': ('MP3', 'OGG', 'WAV', 'AMR'),
        'archives': ('ZIP', 'GZ', 'TAR')
    }

    for category, extensions in categories.items():
        if extension.upper() in extensions:
            return category

    return 'unknown'




# Эта функция process_file отвечает за обработку каждого файла в заданной папке / 
# и перемещение его в соответствующую подпапку, основанную на категории файла. 
# принимает два аргумента: root - корневая директория и file - имя файла./ 
#  Функция возвращает кортеж из двух строк: категория файла и его расширение.
def process_file(root: str, file: str) -> Tuple[str, str]: 
    filename, extension = os.path.splitext(file) # разделяем имя файла на имя файла без расширения (filename) и его расширение (extension).
    category = categorize(extension[1:]) #  Вызываем функцию categorize() для определения категории файла, передавая расширение файла без первичного символа (точки) в качестве аргумента. Результат сохраняется в переменную category.
    new_name = normalize(filename) + extension # Применяем функцию normalize() к имени файла без расширения и добавляем расширение обратно к нормализованному имени. Результат сохраняется в переменную new_name.
    new_path = os.path.join(root, category, new_name) # Создаем новый путь для файла, объединяя корневую директорию, категорию и новое имя файла. Результат сохраняется в переменную new_path.

    if category == 'archives':
        archive_path = os.path.join(root, file) # Создаем путь к архиву, объединяя корневую директорию и имя файла
        target_path = os.path.join(root, category, normalize(filename)) # Создаем целевой путь для содержимого архива, объединяя корневую директорию, категорию и нормализованное имя файла (без расширения).
        os.makedirs(target_path, exist_ok=True) # Создаем папку для распакованного содержимого архива, если она еще не существует (параметр exist_ok=True указывает, что ошибки существующей папки следует игнорировать).
        shutil.unpack_archive(archive_path, target_path) # Распаковываем архив, указанный путем archive_path, в целевую директорию target_path.
    else:
        os.makedirs(os.path.join(root, category), exist_ok=True) # Создаем папку для категории файла, если она еще не существует.
        shutil.move(os.path.join(root, file), new_path) # Перемещаем файл из его текущего местоположения

    return category, extension

root = "6. модуль - работа с файлами"
file = "output.txt"

process_file(root, file)