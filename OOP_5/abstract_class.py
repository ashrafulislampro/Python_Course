from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    
    
    def move(self):
        pass

class Tesla(Car):
    def start(self):
        print("Wow, Abstraction method is hidden the mechanism of Tesla car")
    
    def move(self):
        print("Move the car smothly")
        
        
tesla = Tesla()
tesla.start()
tesla.move()

