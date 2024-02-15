from datetime import datetime
class User:
    def __init__(self,first_name,last_name,phone,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    
    def details(self):
        return f"Name: {self.first_name} {self.last_name} Mobile: {self.phone} Email: {self.email}"
class Driver(User):
    def __init__(self, first_name, last_name, phone, email,v_make, v_model,v_color, v_type):
        super().__init__(first_name, last_name, phone, email)
        self.v_make = v_make
        self.v_model = v_model
        self.v_color = v_color
        self.v_type = v_type

    def details(self):
        return f"{super().details()} Vehicle: {self.v_color} {self.v_make} {self.v_model} {self.v_type}"
class Rider(User):
    def __init__(self, first_name, last_name, phone, email):
        super().__init__(first_name, last_name, phone, email)

    def details(self):
        return f"{super().details()}"
class Route:
    def __init__(self, origin, midway, destination):
        self.origin = origin
        self.midway = midway
        self.destination = destination
    def details(self):
        return f"Origin: {self.origin} Midway: {self.midway} Destination: {self.destination}"
class Drive(Route):
    def __init__(self, origin, leave_time, midway, midway_time, destination, arrival_time):
        super().__init__(origin, midway, destination)
        self.leave_time = leave_time
        self.midway_time = midway_time
        self.arrival_time = arrival_time
    def details(self):
        return f"{super().details()} Leaving Time: {self.leave_time} Midway Stop Time: {self.midway_time} Arrival Time: {self.arrival_time}"
    
def main():
    driver1 = Driver("Rodden", "Bona", "902-902-9029", "W0461260@campus.nscc.ca", "Ford", "AU Falcon", "Yellow", "SUV")
    rider1 = Rider("Jim", "Caddick", "902-555-5555", "JCaddick@gmail.com")
    trip1 = Drive("Antigonish",datetime(2024,2,15,8,0),"Tim Hortons",datetime(2024,2,15,8,30), "Strait Area Campus",datetime(2024,2,15,9,0))

    travel1 = [driver1,rider1,trip1]

    for i in travel1:
        print(i.details())

if __name__ == "__main__":
    main()