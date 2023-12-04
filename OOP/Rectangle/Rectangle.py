class Rectangle:
    length = 0
    breadth = 0
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth


R1 = Rectangle(10,20)
print("Initial length is {}".format(R1.length))
print("Initial breadth is {}".format(R1.breadth))
areaOfR1 = R1.area()
print("Area of rectangle is {} unit square".format(areaOfR1))