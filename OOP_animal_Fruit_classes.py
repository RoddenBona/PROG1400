#This is to demonstrate inhieritance in OOP

#Create the general animal class
class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        pass

#Then at least 1-2 more classes for some animals
class Dog(Animal):
    def speak(self):
        return(f"{self.name} says Woof")
    
class Cat(Animal):
    def speak(self):
        return(f"{self.name} says Meow")
    

#Create objects of a dog and cat
dog = Dog("Kobe")
cat = Cat("Finn")


#Use methods
print(dog.name)
print(cat.name)
print(F"{dog.speak()} and {cat.speak()}")

#The Dog and Cat classes ingierit the name properties of the general Animal class




#Polymorphism in python allows objects of different types to inhierit objects of a common type
class Fruit:
    def __init__(self,name,):
        self.name = name

    #Method to return "generic taste"
    def taste(self):
        return "Generic Taste"

class Apple(Fruit):
    def __init__ (self, name, color):
    #Super is a built in function used usually in OOP
    #Used specifically within classes that are part of an inhieritance hierarchy
    #It provides a way to access and call methods from a superclass (parent class)
    #in a subclass (child class)

        super().__init__(name)
        self.color = color

    def taste(self):
        generic_taste = super().taste() #Calling the superclass method
        return f"{generic_taste} and Crispy"
    
class Orange(Fruit):
    def __init__ (self, name, size):
        super().__init__(name)
        self.size = size

    def taste(self):
        generic_taste = super().taste() #Calling the superclass method
        return f"{generic_taste} and Juicy"

def describe_taste(Fruit):
    print (f"{Fruit.name} tastes: {Fruit.taste()}")

#make instances of Apples and Oranges
apple = Apple("Honeydew", "Yellow")
orange = Orange("Orange", "Large")

#Demonstrate polymorphism by calling the describe taste function with different fruit objects
describe_taste(apple)
describe_taste(orange)