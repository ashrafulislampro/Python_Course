class Laptop:
    def __init__(self, brand, price, color, memory)->None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
        
    def run(self):
        return f"Running laptop : {self.brand}"
    def coding(self):
        return f"Learning python and practicing"
class Phone:
    def __init__(self, brand,price, color, duel_sim)->None:
        self.brand = brand
        self.price = price
        self.color = color
        self.duel_sim = duel_sim
    def run(self):
        return f"Phone tipa tipi kre"
    def phone_call(self, phone, text):
        return f"Sending SMS to: {phone} with text: {text}"
    
class Camera:
    def __init__(self, brand, price, color, pixel)-> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel
        
    def run(self):
        pass
    def change_lens(self):
        pass
    