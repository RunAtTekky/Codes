# Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move")

# Child classes
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Audi", "A8")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(f"{x.brand} {x.model}")
    x.move()
