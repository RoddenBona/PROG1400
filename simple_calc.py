#define a class for advanced calculations
#The @staticmethod decorator is used to define a method within a class
# that does not access or modify the class or instance state
#his meansthat the method does not have access to the instance (self)
# or the class (cls) and behave like a regula function within the class

# When you define a method within a class, by default it is an instance method,
# meaning it operates on an instance of the class and has access to the instance
# attributes via the self parameter. However, sometimes you may want to define a
# method that does not require access to the instance or the class itself.
class AdvancedCalc:
    @staticmethod
    def exponentials(base, exponent):
        return base ** exponent


#define the functions for basic math applications
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by 0")
    else:
        return x / y
    
