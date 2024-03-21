class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        def __str__(self):
            return f"{self.name} is {self.age} years old"

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)

class Parent:
    hair_color = "brown"
    speaks = ["English"]

class Child(Parent):
    hair_color = "purple"

    def __init__(self):
        super().__init__()
        self.speaks.append("German")

if isinstance(miles, Dog) == True:
    print("True")
