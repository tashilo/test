def get_recipe(path, search_id):
    # Используя менеджер контекста для чтения файла
    with open(path, 'r') as file:
        # Чтение строк из файла
        lines = file.readlines()

        # Разбор каждой строки и поиск рецепта с указанным search_id
        for line in lines:
            # Удаление символа конца строки и разделение строк по запятым
            parts = line.strip().split(',')

            # Проверка совпадения search_id с идентификатором рецепта в строке
            if parts[0] == search_id:
                # Создание словаря с информацией о рецепте и возврат его
                recipe = {
                    "id": parts[0],
                    "name": parts[1],
                    "ingredients": parts[2:],
                }
                return recipe

    # Если рецепт с указанным search_id не найден, возврат None
    return None

