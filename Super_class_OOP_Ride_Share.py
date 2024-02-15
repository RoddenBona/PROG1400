class User:
    def __init__(self,first_name,last_name,address,phone,email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
    def __str__(self):
        return  self.__class__.__name__
    def make_drive(self,route):
        print(f"{self.first_name} {self.last_name} is making a trip along the route of:{route}")

class Driver(User):
    def __init__(self, first_name, last_name, address, phone, email,v_make, v_model,v_color, v_type):
        super().__init__(first_name, last_name, address, phone, email)
        self.v_make = v_make
        self.v_model = v_model
        self.v_color = v_color
        self.v_type = v_type

    def get_stops(self, route):
        for stops in range(len(route)):
            if stops [0] or stops[len(route)-1] == False:
                return stops

    def make_drive(self,route):
        print(f"{self.first_name} {self.last_name} is driving a {self.v_color} {self.v_make} {self.v_model} {self.v_type} along the route\
            leaving from {route[0]} and arriving at {route[len(route) -1]} and stopping at {route.get_stops()}") 
class Rider(User):
    def __init__(self, first_name, last_name, address, phone, email):
        super().__init__(first_name, last_name, address, phone, email)
        
    def make_drive(self, route):
        print(f"{self.first_name} {self.last_name} will pick you up along the {route} route")
class Route:
    def __init__(self, stops):
        self.stops = stops
    def __str__(self):
        pass

driver1 = Driver("Rodden", "Bona","36 Summit Dr" ,"902-300-5767","roddenbona2003@gmail.com", "Kia", "Soul", "Yellow", "SUV")
rider1 = Rider("Will", "Williams","10 Existance St" ,"902-9029-029", "W.Williams@hotmail.com")
route = ["Antigonish","Tim Hortons", "Strait Area Campus"]

driver1.make_drive(route)
rider1.make_drive(route)