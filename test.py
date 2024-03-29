import os
import sys
from sys import argv
import shutil
import re
from collections import defaultdict
import zipfile  # для работы с архивами
from pathlib import Path

# Словарь, связывающий расширения файлов и категории
EXTENSIONS = {
    'images': ['jpg', 'png', 'jpeg', 'svg', 'gif', 'bmp', 'tif'],
    'audio': ['mp3', 'ogg', 'wav', 'amr'],
    'video': ['mp4', 'avi', 'mov', 'mkv'],
    'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls', 'pptx', 'rtf'],
    'archives': ['zip', 'tar', 'gz', 'bz2', 'rar'],
}
# Эта переменная предназначена для хранения всех возможных расширений файлов.
ALL_EXTENSIONS = set(ext for exts in EXTENSIONS.values() for ext in exts)

# Множества для хранения известных и неизвестных расширений
KNOWN_EXTENSIONS = set(ext for ext_list in EXTENSIONS.values() for ext in ext_list)
UNKNOWN_EXTENSIONS = set()

FOLDERS_TO_IGNORE = {'images', 'audio', 'video', 'documents', 'archives', 'unknown'}

# Словарь для хранения файлов каждой категории
FILES_IN_CATEGORIES = {
    'images': [],
    'audio': [],
    'video': [],
    'documents': [],
    'archives': [],
    'unknown': []
}

def normalize(name: str) -> str:
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh',
        'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
        'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts',
        'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu',
        'Я': 'Ya'
    }

    result = []
    for simv in name:
        if re.match(r'[a-zA-Z0-9]', simv):
            result.append(simv)
        elif simv in translit_dict:
            result.append(translit_dict[simv])
        else:
            result.append('_')
    return ''.join(result)

def process_files(file_path: Path, target_path: Path):
    file_extension = file_path.suffix.lower()[1:]  # убираем точку и приводим к нижнему регистру

    normalized_name = normalize(file_path.stem) + file_path.suffix

    # определяем категорию файла по его расширению
    for category, extensions in EXTENSIONS.items():
        if file_extension in extensions:
            category_path = target_path / category
            category_path.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(category_path / normalized_name))
            FILES_IN_CATEGORIES[category].append(normalized_name)
            KNOWN_EXTENSIONS.add(file_extension)
            break
    else:
        category = "unknown"
        category_path = target_path / category
        category_path.mkdir(exist_ok=True)
        shutil.move(str(file_path), str(category_path / normalized_name))
        FILES_IN_CATEGORIES[category].append(normalized_name)
        if file_extension not in KNOWN_EXTENSIONS:
            UNKNOWN_EXTENSIONS.add(file_extension)


# Это определение функции process_folder, которая принимает три аргумента: /
#  folder_path (путь к обрабатываемой папке), target_path (путь к целевой папке, куда будут перемещаться файлы) /
#  и is_root_folder (флаг, указывающий, является ли обрабатываемая папка корневой).
def process_folder(folder_path: Path, target_path: Path, is_root_folder=False):
    for item in folder_path.iterdir():
        if item.is_dir():
            # Игнорируем папки с указанными названиями только на верхнем уровне
            if is_root_folder and item.name in FOLDERS_TO_IGNORE:
                continue
            # Рекурсивно обрабатываем вложенные папки
            process_folder(item, target_path)
            if not any(item.iterdir()):
                item.rmdir()  # удаляем пустую папку
        else:
            process_files(item, target_path)

def create_category_folders(path):
    categories = ['images', 'audio', 'documents', 'video', 'archives', 'unknown']
    for category in categories:
        category_path = os.path.join(path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

def unpack_archives(target_folder: str):
    target_folder_path = Path(target_folder)  # преобразование в Path
    archives_path = target_folder_path / 'archives'
    for file in os.listdir(archives_path):
        file_path = os.path.join(archives_path, file)
        try:
            shutil.unpack_archive(file_path, os.path.join(archives_path, file.split('.')[0]))
        except shutil.ReadError:
            print(f"Cannot unpack archive {file_path}. Skipping.")


def main():
    # Получаем путь к папке из аргументов командной строки
    root_folder = argv[1]
    target_folder = argv[2] if len(argv) > 2 else root_folder  # Если не указан, используем root_folder как папку назначения

    # Создаем папки для каждой категории файлов
    create_category_folders(target_folder)
    
    # Обрабатываем все файлы и папки в указанной папке
    process_folder(Path(root_folder), Path(target_folder), is_root_folder=True)

    # После обработки всех файлов, добавим расширения в список неизвестных расширений только если они не уже в списке известных
    for ext in ALL_EXTENSIONS:
        if ext not in KNOWN_EXTENSIONS:
            UNKNOWN_EXTENSIONS.add(ext)
    
    # Распаковываем все архивы
    unpack_archives(target_folder)
    
    # Выводим результаты
    print(f"Processed files in categories: {FILES_IN_CATEGORIES}")
    print(f"Known extensions: {KNOWN_EXTENSIONS}")
    print(f"Unknown extensions: {UNKNOWN_EXTENSIONS}")

if __name__ == "__main__":
    main()