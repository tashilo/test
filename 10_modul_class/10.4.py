class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


    def change_color(self, color):
        Animal.color = color  # Меняем цвет по умолчанию для всего класса, через один из єкземпляров


first_animal = Animal("Kitti", 3)
second_animal = Animal("Baddi", 30)
first_animal.change_color("red")

print(first_animal.color)
print(second_animal.color)