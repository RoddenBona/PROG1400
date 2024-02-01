#Creating a rectangle and define the attributes and methods of it to calculate it's area and perimeter

#define the class. classes are templates for objects
#n its's deffinition is the __init__ method which initializes it's attributes
#the self attribute is a reference to the instacne to the class. Every class needs it
#Length and width are attributes of the class
#We'll be calculating the area and perameter of the rectangle using a calculate_area and calculate_perimeter 
class Rectangle:
    def __init__(self,length,width,heigth):
        self.length = length
        self.width = width
        self.heigth = heigth

    def calculate_area(self):
        return self.length*self.width
    
    def calculate_volume(self):
        return self.length*self.width*self.heigth

    def calculate_perimeter(self):
        return 2*(self.length + self.width)
    
#create an object using the provided class and it's attributes
rect = Rectangle(length = 6, width = 4, heigth= 5)


#access the object's attributes
#We use dot (.) notation to access singular attribures of an object
print(f"Length: {rect.length}")
print(f"Width: {rect.width}")

#print(type(rect))

#Calling object methods
area = rect.calculate_area()
print(f"Area in 2D: {area}")

perimeter = rect.calculate_perimeter()
print(f"Perimeter: {perimeter}")

volume = rect.calculate_volume()
print(f"Volume: {volume}")