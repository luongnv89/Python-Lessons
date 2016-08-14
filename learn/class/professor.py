from human import Human

class Professor(Human):
    """docstring for Professor"""

    domain = 'none'

    def __init__(self, name, age):
        super(Professor, self).__init__(name, age)

    def getDomain(self):
        return self.domain

    def setDomain(self, dom):
        self.domain = dom