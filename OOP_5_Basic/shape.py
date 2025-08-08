from math import pi

class Shape:
    def __init__(self, name)-> None:
        self.name = name
        
        
class Rectangle(Shape):
    def __init__(self, name, length, width)-> None:
        self.length = length
        self.width = width
        super().__init__(name)
        
    def area(self):
         return self.length * self.width
     
class Circle(Shape):
    def __init__(self, name, radius)-> None:
        self.radius = radius
        super().__init__(name)
    def area(self):
        return pi * self.radius * self.radius
    
    
    
shap = Shape("Rectangle")
shap1 = Rectangle("square", 20, 4)
area = shap1.area()
print("Square Area : ", area)


shap2 = Circle("circle", 4)
area = shap2.area()
print("Circle area : ", area)