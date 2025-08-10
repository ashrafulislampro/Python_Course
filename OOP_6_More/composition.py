class Engine:
    def __init__(self):
        pass
    def start(self):
        return "Engin started"

class Driver:
    def __init__(self):
        pass
    
# car "has an" engine
class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()
        
    def start(self):
        self.engine.start()