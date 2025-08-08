# poly --> many (multiple)
# morph --> shape

class Animal:
    def __init__(self, name)-> None:
        self.name = name
    def make_sound(self):
        print("animal making sound")
class Cat(Animal):
    def __init__(self, name)-> None:
        super().__init__(name)
    def make_sound(self):
        print("meow meow")

class Goat(Animal):
    def __init__(self, name)-> None:
        super().__init__(name)
        
    def make_sound(self):
        print("beh beh beh")
        
        
class Dog(Animal):
    def __init__(self, name)-> None:
        super().__init__(name)
    def make_sound(self):
        print("gheu gheu")



don = Cat("Real Don")
# don.make_sound()

dog = Dog("Rocky")
# dog.make_sound()



mess = Goat("L M")
# mess.make_sound()


less = Goat("gora gori")

animals = [don, dog, mess, less]

for animal in animals:
    animal.make_sound() 






