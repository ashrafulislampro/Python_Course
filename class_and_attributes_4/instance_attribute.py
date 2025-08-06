class Shop:
    shopping_mail = "Jamuna Future Park"
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []   # cart is an instance attribute
        
    def add_to_cart(self, item):
        self.cart.append(item)
        
mehjabeen = Shop("Mahjabeen")
mehjabeen.add_to_cart("Shoes")
mehjabeen.add_to_cart("Phone")
mehjabeen.add_to_cart("churi")

print(mehjabeen.cart)

apurvo = Shop("Apurvo")
apurvo.add_to_cart("glass")
apurvo.add_to_cart("Xiomi")
apurvo.add_to_cart("Apple Watch")

print(apurvo.cart)


nisho = Shop("Nisho")
nisho.add_to_cart("Cap")
nisho.add_to_cart("iPhone")
nisho.add_to_cart("Watch")

print(nisho.cart)