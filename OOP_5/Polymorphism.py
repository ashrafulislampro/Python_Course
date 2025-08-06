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


class Dog(Animal):
    def __init__(self, name)-> None:
        super().__init__(name)
    def make_sound(self):
        print("gheu gheu")

def Goat(Animal):
    def __init__(self, name)-> None:
        super().__init__(name)
        
    def make_sound(self, ):
        print("")
        
        
        
        
        
        

don = Cat("Real Don")
don.make_sound()

dog = Dog("Rocky")
dog.make_sound()

dfdf 






