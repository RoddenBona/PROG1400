class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

        def __str__(self):
            return f"{self.name} is {self.age} years old"
        
        def speak(self, sound):
            return f"{self.name} says {sound}"

miles = Dog("Miles", 4,"German Sheppard")
buddy = Dog("Buddy", 9,"Golden Labrador")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")
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

buddy.speak("woof")

