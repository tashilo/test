from collections import UserDict

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data: # Обращение к атрибуту data, в котором хранится словарь
            if self.data[key] == value:
                keys.append(key)
        return keys

# Пример использования
my_dict = LookUpKeyDict(a=1, b=2, c=1)
print(my_dict.lookup_key(1)) # Вывод: ['a', 'c']
