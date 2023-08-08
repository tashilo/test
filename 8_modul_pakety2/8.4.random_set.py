from random import randrange

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min >= quantity or quantity >= max:
        return []

    numbers = set()  # использование множества, чтобы обеспечить уникальность чисел
    while len(numbers) < quantity:
        number = randrange(min, max + 1)  # случайное число в диапазоне от min до max (включительно)
        numbers.add(number)  # добавляем число в множество (если оно уже есть, то ничего не произойдет)

    return sorted(list(numbers))  # преобразуем множество в список и сортируем его

# Тест функции
print(get_numbers_ticket(1, 49, 6))  # например, для лотереи, где нужно угадать 6 чисел от 1 до 49
