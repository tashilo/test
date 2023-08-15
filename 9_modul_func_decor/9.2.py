DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    discount = customer.get("discount", DEFAULT_DISCOUNT)
    new_price = price * (1 - discount)
    
    return new_price

customer1 = {"name": "Dima"}
customer2 = {"name": "Boris", "discount": 0.15}

print(get_discount_price_customer(100, customer1))
print(get_discount_price_customer(100, customer2))