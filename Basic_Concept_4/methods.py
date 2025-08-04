def call():
    print("Calling someone I don't know")
    return "Call done"

class Phone:
    price = 1200
    color = "Blue"
    band = "Samsung"
    features = ["camera", "speaker", "hammer"]
    def call(self):
        print("Call someone")
        
    def send_sms(self,phone, sms):
        text = f"Sending Sms to {phone} and message {sms}"
        return text

my_phone = Phone()
print(my_phone.features)
my_phone.call()
print(my_phone.send_sms(1234556, "pore janabe"))