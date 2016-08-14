from human import Human

class Student(Human):
    """docstring for Student"""

    subjects = []

    def __init__(self, name, age):
        super(Student, self).__init__(name, age)

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getSubject(self):
        return self.subjects

    def joinASubject(self, sb):
        self.subjects.append(sb)

    def finishedASubject(self, sb):
        self.subjects.remove(sb)