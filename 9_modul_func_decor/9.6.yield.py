def generator_numbers(string=""):
    for word in string.split():
        number = ''.join(filter(str.isdigit, word)) # Оставляем только цифры в строке
        if number:
            yield int(number)

def sum_profit(string):
    return sum(generator_numbers(string))

string = "The resulting profit was: from the southern possessions $100, from the northern colonies $500, and the king gave $1000."
print("Numbers found:")
for number in generator_numbers(string):
    print(number)

print("Total profit:", sum_profit(string))
