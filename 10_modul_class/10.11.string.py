from collections import UserString

class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data: # Обращение к атрибуту data, в котором хранится строка
            if char.isdigit():
                count += 1
        return count

# Пример использования
string = NumberString("Тест 1234")
print(string.number_count()) # Вывод: 4