# static attribute  (class attribute)
# static method  (@staticmethod)
# class method  (@classmethod)
# difference between static method vs class method6

class Shopping:
    cart = []  # class attribute, Static attribute
    origin = "China"
    
    def __init__(self, name, location):
        self.name = name # instance attribute
        self.location = location
    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"buying :{item} for price : {price} and remaining : {remaining}")
    
    @staticmethod
    def multiply(a, b):
        # print(self.name) not support instance attribute
        result = a * b
        print(result)
    @classmethod
    def hudai_dekhi(self, item):
        # print(self.name)  support instance attribute
        print("Hudai dekhi kintu kinmu just ac er hawa khaite aschi", item)
        
basundara = Shopping("basu er dhara", "not popular location")
basundara.purchase("lungi", 500,  00) 
# Shopping.purchase(2, 3, 3)
basundara.hudai_dekhi("Lungi")
# Shopping.hudai_dekhi("gamchha")

# static method
Shopping.multiply(3, 6)

# basundara.multiply(4, 3)


