class A:
    name = ''
    age = 0

class B(A):
    height = ''

class C(B):
    weight = ''

    def Read(self):
        print("Please Enter the Following values")
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.height = input("Enter height: ")
        self.weight = int(input("Enter weight: "))
    
    def display(self):
        print("Entered values are as follows")
        print("Name =", self.name)
        print("Age =", self.age)
        print("Height =", self.height)
        print("Weight =", self.weight)

Ob1 = C()

Ob1.Read()
Ob1.display()