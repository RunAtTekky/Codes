class Prac:
    x = 0
    def disp(self,x):
        self.x = x
        print("The value of local variable x is", x)
        print("The value of instance variable x is", x)

ob = Prac()
ob.disp(50)