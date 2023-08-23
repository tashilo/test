from random import randrange


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) == int or type(x) == float:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) == int or type(y) == float:
            self.__y = y

    def __str__(self):
        return f"Point({self.__x},{self.__y})"        
                   

class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:    
            self.coordinates.y = value
        else:
            raise IndexError("Index должен быть 0 или 1")

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Index должен быть 0 или 1")
        
    def __call__(self, value=None):
        if value is not None:
            return (self.coordinates.x * value, self.coordinates.y * value)
        else:
            return (self.coordinates.x, self.coordinates.y)    
        
    def __add__(self, other):
        return Vector(Point(self.coordinates.x + other.coordinates.x, self.coordinates.y + other.coordinates.y))

    def __sub__(self, other):
        return Vector(Point(self.coordinates.x - other.coordinates.x, self.coordinates.y - other.coordinates.y))

    def __mul__(self, other):
        return self.coordinates.x * other.coordinates.x + self.coordinates.y * other.coordinates.y  

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5  
        
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})" 
    
    def __eq__(self, other):
        return self.len() == other.len()

    def __ne__(self, other):
        return self.len() != other.len()

    def __gt__(self, other):
        return self.len() > other.len()

    def __lt__(self, other):
        return self.len() < other.len()

    def __ge__(self, other):
        return self.len() >= other.len()

    def __le__(self, other):
        return self.len() <= other.len()

class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = [Vector(Point(randrange(max_points), randrange(max_points))) for _ in range(max_vectors)]

    def __next__(self):
        if self.current_index >= len(self.vectors):
            raise StopIteration
        vector = self.vectors[self.current_index]
        self.current_index += 1
        return vector

class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)


vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)