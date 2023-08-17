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
print(cat.nickname)


class Dog(Animal):
    def say(self):
        return "Woof"
    
    def __init__(self, nickname, weight, breed, owner):
        super().__init__(nickname, weight)
        self.breed = breed
        self.owner = owner

    def who_is_owner(self):
        return self.owner.info()   



class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address
        }
    
owner = Owner("Tanya", 43, "Odesa")
dog = Dog("Barbos", 23, "labrador", owner)        
print(dog.who_is_owner())    