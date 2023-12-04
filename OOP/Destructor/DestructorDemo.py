class DestructorDemo:
    def __init__(self):
        print("Welcome")
    def __del__(self):
        print("Destructor executed successfully")

Ob1 = DestructorDemo()
Ob2 = Ob1
Ob3 = Ob2

print("Id of Ob1 = ", id(Ob1))
print("Id of Ob2 = ", id(Ob2))
print("Id of Ob3 = ", id(Ob3))

del(Ob1)
del(Ob2)
del(Ob3)