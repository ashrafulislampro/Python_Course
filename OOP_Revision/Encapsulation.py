class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # private variable or attribute
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
            
p = Person("Ashraful", 26)
p.set_age(25)   # Here set_age() method set the age value and the get_age() method return the age value. Otherwise we can't access or control the age variable that's why this is Encapsulation
print(p.get_age())   # Output : 26
        