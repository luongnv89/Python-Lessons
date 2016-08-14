class Human:
    """docstring for Human"""
    def __init__(self, name, age):
        super(Human, self).__init__()
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def sayHello(self):
        print("Hello, I am "+self.name+". I am "+str(self.age)+" years old")