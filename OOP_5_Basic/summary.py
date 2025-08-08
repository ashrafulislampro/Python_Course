class Book:
    def __init__(self, name)-> None:
        self.name = name
    def read(self):
        raise NotImplemented
    
class Physics(Book):
    def __init__(self, name, lab)-> None:
        self.lab = lab
        super().__init__(name)
    def read(self):
        print("Physic lab experiment must be submitted")
        
tapon = Physics("tapon", True)
print(issubclass(Physics, Book))
print(isinstance(tapon, Physics))
print(isinstance(tapon, Book))
tapon.read()
