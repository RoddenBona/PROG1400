import simple_calc

#using functions from the imported module
x = int(input("Enter a number to add: "))
y = int(input("Enter a number to add: "))

#print(f"Answer: {simple_calc.add(x,y)}")

print(f"Addition  {simple_calc.add(x,y)}")
print(f"Subtraction: {simple_calc.subtract(x,y)}")
print(f"Multiply: {simple_calc.multiply(x,y)}")
print(f"Divide: {simple_calc.divide(x,y)}")

calc = simple_calc.AdvancedCalc.exponentials(2,10)

print(calc)