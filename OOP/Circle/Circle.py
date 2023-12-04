class Circle:
    radius = 0
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

C1 = Circle(8)

areaC1 = C1.area()

periC1 = C1.perimeter()

print("Area of Circle C1 is", areaC1)
print("Perimeter of Circle C1 is", periC1)


C5 = Circle(10)
print("Area of circle is", C5.area(), "Peri of circle is", C5.perimeter())
