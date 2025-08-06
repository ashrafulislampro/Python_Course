# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class

class Gadget:
    def __init__(self, brand, price, color, origin)->None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    def run(self):
        return f"Running laptop : {self.brand}"


class Laptop:
    def __init__(self, memory, ssd)->None:
        self.memory = memory
        self.ssd = ssd
    def coding(self):
        return f"Learning python and practicing"
class Phone(Gadget):
    def __init__(self,brand, price, color, origin, duel_sim)->None:
        self.duel_sim = duel_sim
        super().__init__(brand, price, color, origin)
    def phone_call(self, phone, text):
        return f"Sending SMS to: {phone} with text: {text}"
    def __repr__(self)-> str:
        return f"Phone : {self.brand}, {self.price}, {self.origin}, {self.duel_sim}"
    
class Camera:
    def __init__(self, pixel)-> None:
        self.pixel = pixel
    def change_lens(self):
        pass



# inheritance
my_phone = Phone("iPhone", 120000, "Silver", "China", True)
print(my_phone)