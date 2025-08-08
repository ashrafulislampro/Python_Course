# encapsulation --> hide details
# access modifier : public, protected, private




class Bank:
    def __init__(self, holder_name, initial_deposit)-> None:
        self.holder_name = holder_name  # Public Attribute
        self._branch = "Banani 11"      # Protected Attribute
        self.__balance = initial_deposit # Private Attribute   
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f"Fokir taka nai"
        
rafsun = Bank("Chooto bro", 10000)
print(rafsun.holder_name)
rafsun.holder_name = "Boro vai"
rafsun.balance = 0
rafsun.deposit(40000)
# rafsun.__balance = 0
print(rafsun.get_balance())
print(rafsun.holder_name)
# print(dir(rafsun))
print(rafsun._Bank__balance)