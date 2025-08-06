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
class Phone:
    def __init__(self, duel_sim)->None:
        self.duel_sim = duel_sim
    def phone_call(self, phone, text):
        return f"Sending SMS to: {phone} with text: {text}"
    
class Camera:
    def __init__(self, pixel)-> None:
        self.pixel = pixel
    def change_lens(self):
        pass
    