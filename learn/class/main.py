from student import Student
from professor import Professor

s1 = Student('Hung', 13)
s1.setId(1234)
s1.joinASubject('Math')

s2 = Student('Mai', 27)
s2.setId(456)
s1.joinASubject('English')

p1 = Professor('Luong', 28)
p1.setDomain('Math')

s1.sayHello()
print('s1 id: ' + str(s1.getId()))
print('s1 subjects: ' + str(s1.getSubject()))

s2.sayHello()
print('s2 id: ' + str(s2.getId()))
print('s2 subjects: ' + str(s2.getSubject()))

p1.sayHello()
print('p1 domain: ' + p1.getDomain())