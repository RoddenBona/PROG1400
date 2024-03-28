import math

#PART 1 ABSTACTION
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
class Animal:
    def __init__(self):
        return self.__class__.__name__
    def speak(self):
        pass
    def move(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        return f"woof!"
    def move(self):
        return f"Dog runs away"

class Cat(Animal):
    def __init__(self,):
        super().__init__()
    def speak(self):
        return f"meow!"
    def move(self):
        return f"Cat scitters away"

class Bird(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        return f"tweet tweet!"
    def move(self):
        return f"Bird flys away"
    
mybird = Bird
mydog = Dog
mycat = Cat

def speaking(Animal):
    print(Animal.speak(Animal))

def moving(Animal):
    print(Animal.move(Animal))

speaking(mydog)
speaking(mycat)
speaking(mybird)

moving(mydog)
moving(mycat)
moving(mybird)

#PART 4 POLYMORPHISM

class Vehicle:
    def __init__(self):
        return self.__class__.__name__
    def traveling(self):
        pass

class Car(Vehicle):
    def __init__(self):
        super().__init__()
    def travelingl(self):
        return f"The car starts up an drives 30km"

class Plane(Vehicle):
    def __init__(self):
        super().__init__()
    def traveling(self):
        return f"The plane fires up and flies 3000km"

class Bike(Vehicle):
    def __init__(self):
        super().__init__()
    def traveling(self):
        return f"The bike is out and cycles 3km"
    
mycar = Car
myplane = Plane
mybike = Bike

def journey(Vehicle):
    print(Vehicle.traveling(Vehicle))

journey(mycar)
journey(myplane)
journey(mybike)