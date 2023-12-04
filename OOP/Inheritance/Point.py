class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

class New_Point(Point):
    def draw(self):
        print(f"Locate Point X = {self.x} on X axis")
        print(f"Locate Point Y = {self.y} on X axis")

P = New_Point()
P.set_coordinates(10,20)
P.draw()
