class methodOverloading:
    def greeting(self, name=None):
        if name is not None:
            print(f"Welcome {name}")
        else:
            print("Welcome")


ob1 = methodOverloading()

ob1.greeting("Varun")
ob1.greeting()