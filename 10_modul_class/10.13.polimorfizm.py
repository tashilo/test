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


class CatDog:
    def __init__(self, nickname, weight):
        self.cat = Cat(nickname, weight)

    def say(self):
        return self.cat.say()

    def change_weight(self, weight):
        return self.cat.change_weight(weight)

    # Доступ к атрибутам nickname и weight можно предоставить через свойства
    @property
    def nickname(self):
        return self.cat.nickname

    @property
    def weight(self):
        return self.cat.weight
