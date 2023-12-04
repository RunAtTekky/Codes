class Demo:
    result = 0
    def add(self, instanceOf=None, *args):
        if instanceOf == 'int':
            self.result = 0
        if instanceOf == 'str':
            self.result = ''
        for i in args:
            self.result += i
        return self.result
    
ob1 = Demo()
print(ob1.add('int', 10, 20 ,30))
print(ob1.add('str', 'I', 'Love', 'Python', 'Programming'))
    