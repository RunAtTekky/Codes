class Rectangle:
    length = 0
    breadth = 0

R1 = Rectangle()
print("Initial length is {}".format(R1.length))
print("Initial breadth is {}".format(R1.breadth))

R1.length = 20
R1.breadth = 30

print("Final length is {}".format(R1.length))
print("Final breadth is {}".format(R1.breadth))
area = R1.length*R1.breadth
print("Area now is {}".format(area))
