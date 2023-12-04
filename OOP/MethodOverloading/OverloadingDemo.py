class Overload:
    def add(self, a, b):
        print(a+b)
    def add(self, a, b, c):
        print(a+b+c)


ob1 = Overload()
ob1.add(7,9)
ob1.add(7,9,3)