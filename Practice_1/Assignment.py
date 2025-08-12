"""
   1.  Create a Product class and a Shop class.
   
   2.  Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.
   
   3.  Inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.
   
   4.  What is Inheritance? Explain with examples
   
   5.  What are Encapsulation and Access Modifiers? Explain with examples

"""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        # print("Product: ", )
        self.products.append(product)
    
    def buy_product(self, name):
        for item in self.products:
            if item.name == name:
                if  item.quantity > 0:
                    item.quantity -= 1
                    print("Congrats, You can buy the product")
                    return
                else:    
                    print("Sorry, Stock out this product")         
                    return
        print("Sorry, Stock out this product")
            

shop = Shop("Mubarak Proprietor Shop")
shop.add_product("Watch", 200, 3)
shop.add_product("Cap", 100, 5)
shop.add_product("Glass", 250, 6)

shop.buy_product("Laptop")







        