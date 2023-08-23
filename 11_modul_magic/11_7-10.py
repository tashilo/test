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




point = Point(1, 10)
vector = Vector(point)

print(point)  # Point(1,10)
print(vector)  # Vector(1,10)
print(vector())  # (1, 10)
print(vector(5))  # (5, 50)

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)
print(vector1 == vector2)  # False
print(vector1 != vector2)  # True
print(vector1 > vector2)  # False
print(vector1 < vector2)  # True
print(vector1 >= vector2)  # False
print(vector1 <= vector2)  # True