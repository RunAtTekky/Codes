class CmpOp:
    def __init__(self,x):
        self.x = x
    
    def __lt__(self,other):
        print("The value of Ob1 =", self.x)
        print("The value of Ob2 =", other.x)
        print("Ob1 < Ob2 :",end='')
        return self.x < other.x
    
    def __gt__(self, other):
        print("Ob1 > Ob2 :", end='')
        return self.x > other.x
    
    def __le__(self, other):
        print("Ob1 <= Ob2 : ",end='')
        return self.x <= other.x
    

Ob1 = CmpOp(50)
Ob2 = CmpOp(60)

print(Ob1 < Ob2)
print(Ob1 > Ob2)
print(Ob1 <= Ob2)