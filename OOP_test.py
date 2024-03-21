#Object Oriented Programming first actual class. Will put this in a new repository soon


#Constructor method initalies the object's attributes.
#This example sets the brand, model, color, and engine state of the cars
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.is_running = False

#method to start the car
    def start_engine(self):
        self.is_running = True
        print(f"The {self.brand} {self.model}'s engine is running")       

#Stopping the engine
    def stop_engine(self):
        self.is_running = False
        print(f"The {self.brand} {self.model}'s engine has stopped")


#Creating objects
#Object oriented approach is to create an instance of the  class by making an object
car1 = Car("Ford", "F150", "Blue")
car2 = Car("Daihatsu", "Applause", "Yellow")

print(car2.color)


#list
car_1 = ["Ford", "F150", "Blue"]
car_2 = ["Daihatsu", "Applause", "Yellow"]

print(car_1[0])

car1.start_engine()
car2.start_engine()
car1.stop_engine()

print(car2.is_running)



#Commented out code for avoid complications
"""
#Inheritance:
#Parent class
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat


#child classes / sub-classes
class Dog(Animal):
    def speak(self):
        return f"{self.name}. Says woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} Says meow"
    
#using methods
dog = Dog("Sampson","domestic")
cat = Cat("Izzy", "domestic")

print(dog.speak())
print(cat.speak())

print(dog.habitat)
print(cat.habitat)
""" 