class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x   
    
    @x.setter
    def x(self, point_x):
        self.__x = point_x 
            
    
    @property
    def y(self):
        return self.__y  

    @y.setter
    def y(self, point_y):
        self.__y = point_y         

point = Point(5, 10)


print(point.x)  # 5
print(point.y)  # 10   