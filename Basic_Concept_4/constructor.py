class Phone:
    manufacture = "China"
    def __init__(self,owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
        
    def send_sms(self, phone, sms):
        text = f"Sending to {phone} and message {sms}"
        print(text)
        
    
my_phone = Phone("Kala chan", "Oppo", 1980)
print(my_phone.brand, my_phone.owner, my_phone.price)

her_phone = Phone("she is my jan", "iPhone", 120000)
print(her_phone.brand, her_phone.owner, her_phone.price)

abbu_phone = Phone("Abbu", "Nokia", 1200)
print(abbu_phone.brand, abbu_phone.owner, abbu_phone.price)

my_phone.send_sms(90384, "Pore nibo")
her_phone.send_sms(2345678, "Akhone lagbe")
abbu_phone.send_sms(10987643, "lagbe nah")