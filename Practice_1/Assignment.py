"""
   1.  Create a Product class and a Shop class.
   
   2.  Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.
   
   3.  Inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.
   
   4.  What is Inheritance? Explain with examples
   
   5.  What are Encapsulation and Access Modifiers? Explain with examples

"""

class Shop:
    def __init__(self, name):
        self.name = name
        self.cart = []
        
    def add_product(self, price, quantity):
        self.price = price
        self.quantity = quantity
        


class Product(Shop):
    pass