#global variable
balance = 1000

def buy_things(item, price):
    # local variable scope
    dream_item = "MaC-book"
    # you can access global variable without using global keyword
    # But if you want to modify the global variable, you need to use the global keyword
    
    global balance
    print(f"previous balance: ", balance)
    balance = balance - price
    print(f"after buying {item}, new balance: ", balance)
    
    
buy_things("book", 200)