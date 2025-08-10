# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.



class User:
    def __init__(self, name, age, money):
        self.name = name
        self._age = age
        self.__money = money
    
    # getter without any setter is readonly attribute
    @property       # using as a method like an attribute
    def age(self):
        return self._age
    
    
    # getter 
    @property
    def salary(self):
        return self.__money
    
    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return "can't add negative value"
        else:
            self.__money += value
    
    
samsu = User("kopa", 21, 12000)
print(samsu.age)  # attribute
# print(samsu.age()) # method

# print(samsu.salary())  # method
print(samsu.salary)
samsu.salary = 10000
print(samsu.salary)