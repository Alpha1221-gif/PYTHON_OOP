# ----CODE1---- #
# Different classes with the same method:

class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")

class boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail!")

class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")

car_ = car("Ford", "Mustang")
boat_ = boat("Ibiza", "Touring 20")
plane_ = plane("Boeing", "747")

for x in (car_,boat_,plane_):
  x.move()
'''Drive!
Sail!
Fly!'''


# Inheritance Class Polymorphism
# ----CODE2---- #
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

class car(vehicle):
    pass

class boat(vehicle):
    def move(self):
        print("Sail!")

class plane(vehicle):
    def move(self):
        print("Fly!")

car_ = car("Ford", "Mustang")
boat_ = boat("Ibiza", "Touring 20")
plane_ = plane("Boeing", "747")

for x in (car_,boat_,plane_):
    print(x.brand)
    print(x.model)
    x.move()
'''Ford
Mustang
Move!
Ibiza
Touring 20
Sail!
Boeing
747
Fly!'''