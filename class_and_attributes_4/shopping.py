class Shopping:
    shop = "Agura"
    amount = 0
    def __init__(self, name):
        self.name = name
        self.cart = []
    def add_to_cart(self, item, price, quantity):
        product = {"item":item, "price": price, "quantity": quantity}
        self.cart.append(product)
    def remove_item(self, item):
        total = 0
        for goods in self.cart:
            if goods["item"] == item:
               del goods
            else:
                total += goods["price"] * goods["quantity"]
        print(f"After Removing item then your total Price : {total}")
        if self.amount < total:
            print(f"Please provide more {total - self.amount} money")
        else:
            print(f"Here is your extra money {self.amount - total}")
            
    def checkout(self, amount):
        total = 0
        self.amount = amount
        for item in self.cart:
            total += item["quantity"] * item["price"]
        print("Your total money : ", total)
        if amount < total:
            print(f"Please provide more {total - amount} money")
        else:
            print(f"Here is your extra money {amount - total}")
        
        
alen_shapon = Shopping("Alen Shapon")
alen_shapon.add_to_cart("Alu", 10, 10)
alen_shapon.add_to_cart("Badam", 20, 5)
alen_shapon.add_to_cart("onion", 5, 15)


alen_shapon.checkout(1000)
alen_shapon.remove_item("Alu")