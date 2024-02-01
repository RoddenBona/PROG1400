import math

#This file is just built off of the previous Basic class file. ust with Inhieritance in it

#Creating a rectangle and define the attributes and methods of it to calculate it's area and perimeter
#define the class. classes are templates for objects
#n its's deffinition is the __init__ method which initializes it's attributes
#the self attribute is a reference to the instacne to the class. Every class needs it
#Length and width are attributes of the class
#We'll be calculating the area and perameter of the rectangle using a calculate_area and calculate_perimeter 


class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
    def volume(self):
        pass
class Rectangle:
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.length*self.width
    
    def calculate_volume(self):
        return self.length*self.width*self.height

    def calculate_perimeter(self):
        return 2*(self.length + self.width)
    
#create an object using the provided class and it's attributes
rect = Rectangle(length = 6, width = 4, height= 5)

#access the object's attributes
#We use dot (.) notation to access singular attribures of an object
print(f"Rectangle Length: {rect.length}")
print(f"Rectangle Width: {rect.width}")
print(f"Rectangle Height: {rect.height}")

#print(type(rect))

#Calling object methods
area = rect.calculate_area()
print(f"Area: {area}")

perimeter = rect.calculate_perimeter()
print(f"Perimeter: {perimeter}")

volume = rect.calculate_volume()
print(f"Volume: {volume}")

#Create a new class called Square which will inhierot te attributes of Retangle
class Sqaure(Rectangle):
    def __init__(self, side_length):
        #Call the constructor of the base class (Rectangle)
        #But instead we are inserting our own extra thing. Where we make the lengh,width, and heigth equal to the one side length variable.
        super().__init__(length = side_length, width=side_length, height=side_length)

#Make te instnce of the square class
#But now we only need tp fill one variable as side_length will just fill in
#the 3 measuremnt variables that it inhierited with itself.
cube = Sqaure(side_length = 3)

print(f"Cube Side Length; {cube.length} ")

#we can use the same methods we made for the original Rectangle class since we inhierited them
area_squared = cube.calculate_area()
print(f"Square Area: {area_squared}") 

volume_squared = cube.calculate_volume()
print(f"Square Volume: {volume_squared}")

perimeter_squared = cube.calculate_perimeter()
print(f"Square Perimeter: {perimeter_squared}")


#Circle class including radius an height attributes
class Circle:
    def __init__(self,radius,height):
        #Only need 2 attributes to do everything below
        self.radius = radius
        self.height = height

#We imported the math funtion in order to do math with circle
#Python does not have pi baked in
    def circle_area_calc(self):
        return math.pi * pow(self.radius, 2)
    
#Area of a sphere
    def sphere_area_calc(self):
        return 4 * math.pi * pow(self.radius, 2)
    
#Volume of a cylinder
    def cylinder_volume_calc(self):
        return math.pi * pow(self.radius, 2) * self.height
    
#Circle Diameter
    def diameter_calc(self):
        return (math.pi * pow(self.radius, 2)) *2
    
#Perimeter calc
    def perimeter_circ(self):
        return 2 * math.pi * self.radius
    

#Now we make a circle object. Giving a value to it's attributes
circ = Circle(radius = 3, height = 2)
print(f"Radius: {circ.radius}")
print(f"Cylinder Height")

#Now we call th metods of calculation

#Diameter calc
diameter = circ.diameter_calc()
print(f"Diaeter of Circle: {diameter}")

#Perimeter calc
circ_perimeter = circ.perimeter_circ()
print(f"Circle Perimeter: {circ_perimeter}")

#Area of a circle
area_circ = circ.circle_area_calc()
print(f"Circle Area: {area_circ}")

#Sphere area if it was one
area_sphere = circ.sphere_area_calc()
print(f"Sphere Area: {area_sphere}")

#and cyliner volume if it was one
area_cylinder = circ.cylinder_volume_calc()
print(f"Cylinder Volume: {area_cylinder}")


#Polymorphism section
#This allows objects of different classes to be treated as objects of a single, common base class
#Allowing you to easily resued old code and add new code without breaking the whole program or wasting time

#Polymorphism enables a "sigle interface" to represent diferent typs of objects

