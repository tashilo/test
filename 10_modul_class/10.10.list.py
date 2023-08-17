from collections import UserList

class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for value in self.data: # Обращение к атрибуту data, в котором хранится список
            if value > 0:
                sum = sum + value
        return sum

# Пример использования
payment = AmountPaymentList([1, -3, 4])
print(payment.amount_payment()) # Вывод: 5
