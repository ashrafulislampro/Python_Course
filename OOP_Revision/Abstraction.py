from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return pi * self.radius * self.radius

c = Circle(5)
print(c.area()) # user only call the area method and don't provide anything as argument this is Abstraction

