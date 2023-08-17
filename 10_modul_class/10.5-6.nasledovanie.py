class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Cat(Animal):
    def say(self):
        return "Meow"    

cat = Cat("Simon", 10)     
print(cat)


class Dog(Animal):
    def say(self):
        return "Woof"
    
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed


dog = Dog("Barbos", 23, "labrador")        
print(dog)