#define the functions for basic math applications

class AdvancedCalc:
    pass


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
    
def exponent(x,y):
    return x ** y

