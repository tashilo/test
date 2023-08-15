def create_car_maker(model_name):
    def car_maker(color):
        print(f"Производим автомобиль {model_name} цвета {color}!")
    
    return car_maker

make_sedan = create_car_maker("Седан")
make_suv = create_car_maker("Внедорожник")
make_lanos = create_car_maker("Ланос")

make_sedan("красный")  # Выведет: Производим автомобиль Седан цвета красный!
make_sedan("Белый")
make_suv("черный")     # Выведет: Производим автомобиль Внедорожник цвета черный!
make_suv("Белый")
make_lanos("Зеленый")
create_car_maker("Ланос")("Синий")

# Расчет числа Фибоначи

def caching_fibonacci():
    cache = {0: 0, 1: 1}
    def fibonacci(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n -2)
        return cache[n]
    
    return fibonacci


# Получаем функцию для вычисления числа Фибоначчи
fib = caching_fibonacci()

# Выводим первые 10 чисел Фибоначчи
for i in range(10):
    print(fib(i))