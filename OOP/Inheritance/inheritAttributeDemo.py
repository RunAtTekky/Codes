class A:
    i = 0
    j = 0

    def showij(self):
        print(f"i = {self.i} j = {self.j}")

class B(A):
    k = 0
    def showijk(self):
        print(f"i = {self.i} j = {self.j} k = {self.k}")
    def sum(self):
        print(f"i + j + k = {self.i + self.j + self.k}")

Ob1 = A()
Ob2 = B()

Ob1.i = 100
Ob1.j = 200
print('Contents of Obj1')
Ob1.showij()
Ob2.i = 100
Ob2.j = 200
Ob2.k = 300
print('Contents of Obj2')
Ob2.showijk()