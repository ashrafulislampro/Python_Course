class Animal:
    def speak(self):
        print("Animal makes a sound")
    
class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.speak() # Output : Animal makes a sound
dog.bark()  # Output: Dog barks

# Above the Dog class have not the speak() method yet access or use the speak() method from the Dog class. So this is inheritance

