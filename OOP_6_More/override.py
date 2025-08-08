class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def eat(self):
        print("vat, monso, dim")
    
    def exercise(self):
        raise NotImplementedError
    
    
class Cricketer(Person):
    def __init__(self,name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)
    
    #  Override method
    def eat(self):
        print("Vegetables")
    
    def exercise(self):
        print("gym a poisha dia ajothai gam jrai")
    
    #  + Sign operator overload
    def __add__(self, other):
        return self.age + other.age

    #  * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight
    #  len overload
    def __len__(self):
        return self.height 
    
    # greater than overload
    def __gt__(self, other):
        return self.age > other.age

sakib = Cricketer("Sakib", 38, 68, 80, "BD")
mushi = Cricketer("Moshi", 36, 65, 70, "BD")
# sakib.eat()
# sakib.exercise()  

# Plus sign overload
print(45+63)
print("Sakib "+ "Rakib")
print([23, 45] + [34, 56, 34, 67])
print(sakib+mushi)
print(sakib * mushi)
print(len(sakib))
print(sakib > mushi)
