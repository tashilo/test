def discount_price(discount):
    def calculate_price(price):
        return price * (1 - discount)
    return calculate_price


cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100


print(cost_15(price))
print(cost_10(price))
print(cost_05(price))