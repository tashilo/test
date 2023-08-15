from functools import reduce


def sum_numbers(numbers):
    return reduce((lambda x, y: x + y), numbers)


numbers = [3, 4, 6, 9, 34, 12]

print(sum_numbers(numbers))


# 9.12


payment = [1, -3, 4]

def amount_payment(payment):
    return reduce(lambda sum, value: sum + (value if value > 0 else 0), payment, 0)

print(amount_payment(payment))  # Выводит 5
