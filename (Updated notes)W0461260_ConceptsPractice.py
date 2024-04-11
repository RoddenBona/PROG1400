"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1400
Repository: https://github.com/RoddenBona/PROG1400
Project: OOP Concepts Practice
Version 1.0
Last Edited: April 11 2024 2024
"""

import math

#PART 1 ABSTACTION
#the process of hiding the implementation details and showing only essential featues of the object
class Shape: #First I define the basic shape class, nothing needs to be in it
    def __init__(self,):
        return self.__class__.__name__
    def area(self):
        pass

class Square(Shape): #Then we can make a subclass of the main shape class with it's own unique traits and instances
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self): #This will overide the main classes area functiom with this one.
        return self.width*self.width
    
class Circle(Shape): #Doing the same here. Using a different shape to differentiae the two
    def __init__(self, radius):
        self.radius = radius
    def area(self): #This will also overide the main area function
        return math.pi * self.radius**2
    
#Now we define 2 objects, one with each subclass o shape
mysquare = Square(12, 11)
mycircle = Circle(5)

#This function will simply print the area of th specific hape, using their respective area function
def print_area(Shape):
    print(f"Area = {Shape.area()}")

print_area(mysquare)
print_area(mycircle)

#PART 2 ENCAPSULATION
#Hiding some of the important details of a class from other objects. and provide a public interface to access them
class Student: #First I define the main class.
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def student_details(self): #This function will return the following string.
        return f"Name: {self.name} Age: {self.age} Grade: {self.grade}"
    
#Now we make a new object of the Student class, filling out it's perameters
mark = Student("Mark",20,75)

#Similar printing function to the encapsulation one
def show_details(self):
    print(Student.student_details(self))

show_details(mark)

#But we're oning to change and update the perameters
mark.age = 21
mark.grade = 90

show_details(mark)

#PART 3 INHERITANCE
#Having a base class that can give it's properties and behaviors to a subclass made from it


#Defining 3 subclasses each of a different animal
# all with a main animal class


#This is thhe main animal class. It really only servers to inheirit the speak and move functions 
#So that they can be overwritten by the subclasses
class Animal:
    def __init__(self):
        return self.__class__.__name__
    def speak(self):
        pass
    def move(self):
        pass

#Simple Dog class
class Dog(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        return f"woof!"
    def move(self):
        return f"Dog runs away"

#3cat class
class Cat(Animal):
    def __init__(self,):
        super().__init__()
    def speak(self):
        return f"meow!"
    def move(self):
        return f"Cat scitters away"

#Bird class
class Bird(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        return f"tweet tweet!"
    def move(self):
        return f"Bird flys away"
    

#Assign variable to be one of each of the 3 subclasses
mybird = Bird
mydog = Dog
mycat = Cat

#Define a function to print what the speak and move function return
def speaking(Animal):
    print(Animal.speak(Animal))

def moving(Animal):
    print(Animal.move(Animal))

#Examples of what they all now say
speaking(mydog)
speaking(mycat)
speaking(mybird)

moving(mydog)
moving(mycat)
moving(mybird)

#PART 4 POLYMORPHISM
#Calling an objects type for the purpose of using one function in different ways depending on various factors

#Main vehicle class
class Vehicle:
    def __init__(self):
        return self.__class__.__name__
    def traveling(self):
        pass

#Car subclass
class Car(Vehicle):
    def __init__(self):
        super().__init__()
    def travelingl(self):
        return f"The car starts up an drives 30km"

#plane subclass
class Plane(Vehicle):
    def __init__(self):
        super().__init__()
    def traveling(self):
        return f"The plane fires up and flies 3000km"

#bike subclass
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
    def traveling(self):
        return f"The bike is out and cycles 3km"

#Just like before. We now create 3 objects, each of a dfferent class
mycar = Car
myplane = Plane
mybike = Bike


#all three will use the travel function
def travel(Vehicle):
    print(Vehicle.traveling(Vehicle))

travel(mycar)
travel(myplane)
travel(mybike)