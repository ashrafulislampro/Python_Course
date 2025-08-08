class Bird:
    def sound(self):
        print("Birds chirp")
    
class Duck(Bird):
    def sound(self):
        print("Duck quacks")
    
class Parrot(Bird):
    def sound(self):
        print("Parrot talks")
        
# Polymorphism in action
def make_sound(bird):
    bird.sound()
duck = Duck()
parrot = Parrot()

make_sound(duck)    # Output: Duck quacks
make_sound(parrot)  # Output: Parrot talks

# Above the make_sound() function is same but sound() method behaves different for different class or object. that is Polymorphism