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
        
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})" 




point = Point(1, 10)
vector = Vector(point)

print(point)  # Point(1,10)
print(vector)  # Vector(1,10)
print(vector())  # (1, 10)
print(vector(5))  # (5, 50)