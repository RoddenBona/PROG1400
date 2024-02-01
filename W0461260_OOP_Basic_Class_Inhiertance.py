#This file is just built off of the previous Basic class file. ust with Inhieritance in it

#Creating a rectangle and define the attributes and methods of it to calculate it's area and perimeter

#define the class. classes are templates for objects
#n its's deffinition is the __init__ method which initializes it's attributes
#the self attribute is a reference to the instacne to the class. Every class needs it
#Length and width are attributes of the class
#We'll be calculating the area and perameter of the rectangle using a calculate_area and calculate_perimeter 
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
print(f"Length: {rect.length}")
print(f"Width: {rect.width}")
print(f"Height: {rect.height}")

#print(type(rect))

#Calling object methods
area = rect.calculate_area()
print(f"Area in 2D: {area}")

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
cube = Sqaure(side_length=3)

#we can use the same methods we made for the original Rectangle class since we inhierited them
area_squared = cube.calculate_area()
print(f"Square Area: {area_squared}") 

volume_squared = cube.calculate_volume()
print(f"Square Volume: {volume_squared}")

perimeter_squared = cube.calculate_perimeter()
print(f"Square Perimeter: {perimeter_squared}")