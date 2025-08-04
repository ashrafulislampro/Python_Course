class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
        
    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"Fokira. You can't withdraw below {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"Bank Fokir haia jabe. You can't withdraw more than {self.max_withdraw}")
        else:
            self.balance -= amount
            print(f"Here is your amount = {amount}")
            print(f'Your current balance is = {self.get_balance()}')
            
brac = Bank(150000)
brac.withdraw(10000)
brac.withdraw(90)