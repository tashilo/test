from decimal import Decimal, getcontext

def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count  # Устанавливаем необходимую точность
    total = Decimal(0)
    for number in number_list:
        total += Decimal(number)
    avg = total / len(number_list)
    
    # Округляем до необходимого количества знаков после запятой
    result = avg.quantize(Decimal('1.' + '0' * (signs_count - len(str(avg).split('.')[0]))))
    
    return result


print(decimal_average([3, 5, 77, 23, 0.57], 6))
print(decimal_average([31, 55, 177, 2300, 1.57], 9))
