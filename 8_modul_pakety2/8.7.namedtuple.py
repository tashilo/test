import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

def convert_list(cats):
    if all(isinstance(cat, Cat) for cat in cats):  # Проверяем, являются ли все элементы списка именованными кортежами
        return [{"nickname": cat.nickname, "age": cat.age, "owner": cat.owner} for cat in cats]
    elif all(isinstance(cat, dict) for cat in cats):  # Проверяем, являются ли все элементы списка словарями
        return [Cat(cat["nickname"], cat["age"], cat["owner"]) for cat in cats]
    else:
        return []  # Возвращаем пустой список, если входной список содержит смешанные типы или пуст



if __name__ == '__main__':
    cats = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
    print(convert_list(cats))
    cats = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
    print(convert_list(cats))