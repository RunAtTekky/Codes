class OprOverLoading:
    def __init__(self, x):
        self.x = x
    
    def __add__(self,other):
        print("The value of Ob1 =", self.x)
        print("The value of Ob2 =", other.x)
        print("The addition of two objects is: ", end='')
        return (self.x+other.x)

Ob1 = OprOverLoading(20)
Ob2 = OprOverLoading(30)

Ob3 = Ob1 + Ob2
print(Ob3)