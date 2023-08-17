class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass 

    def change_weight(self, new_weight): # метод меняющий вес животного
        self.weight = new_weight        


animal = Animal("Kitti", 3) 
animal.change_weight(5) 

print(animal.weight)