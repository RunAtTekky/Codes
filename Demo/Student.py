class Student:

    def __init__(self, name, age, marks) -> None:
        self.name = name
        self.age = age
        self.marks = marks
    
    def menu():
        print("Welcome! Please select an option:")
        print("1. Get names of all students")
        print("2. Get CGPA of all students")
        print("3. Get average of class")
    
def get_max_CGPA(a,b,c):
    if (a.marks > b.marks):
        if (a.marks > c.marks):
            return a
        else:
            return c
    elif (b.marks>c.marks):
        return b
    else:
        return c


Divy = Student("Divy", 20, 8.0)
Irish = Student("Irish", 20, 7.4)
Varun = Student("Varun", 20, 8.6)

maxCGPAstudent = get_max_CGPA(Divy,Irish,Varun)

print(f"Student {maxCGPAstudent.name} has max CGPA {maxCGPAstudent.marks}")

isRunning = True

while (isRunning):
    Student.menu()



