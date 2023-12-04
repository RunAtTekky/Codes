class Parrot():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sing(self, song):
        return "{} sings {}".format(self.name,song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)

# Blue = Parrot("Blue", 20)
# Film = Parrot("Film", 19)

# print(Blue.sing("'Tere naam'"))
# print(Blue.dance())

# print(Film.sing("'Rang laga de re'"))
# print(Film.dance())