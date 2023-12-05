from abc import ABC, abstractclassmethod
class Polygon(ABC):
    @abstractclassmethod
    def noOfSides(self):
        pass

class Triangle(Polygon):
    def noOfSides(self):
        print("I have 3 sides")

class Pentagon(Polygon):
    def noOfSides(self):
        print("I have 5 sides")

class Hexagon(Polygon):
    def noOfSides(self):
        print("I have 6 sides")

class Quadrilateral(Polygon):
    def noOfSides(self):
        print("I have 4 sides")


t = Triangle()
t.noOfSides()

q = Quadrilateral()
q.noOfSides()

p = Pentagon()
p.noOfSides()

h = Hexagon()
h.noOfSides()