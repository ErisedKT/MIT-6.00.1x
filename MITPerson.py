from Person import Person
from Grades import Grades

class MITPerson(Person):
    nextIdNum = 0  # next ID number to assign
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.name + " says:" + utterance)

'''    
m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3, 5, 14, 84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2, 3, 4, 83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1, 10, 28, 55)

MITPersonList = [m1, m2, m3]

for e in MITPersonList:
    print(e)
    
print()
    
MITPersonList.sort()

for e in MITPersonList:
    print(e)
    
p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')
'''

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
        
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, " Yo Bro, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)


s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo di Caprio')
s5 = TransferStudent('Robert deNiro')

studentList = [s1, s2, s3, s4, s5]
'''
print(s1)
print(s1.getClass())
print(s1.speak('where is the quiz?'))
print(s2.speak('I have no clue!'))
'''
'''
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')
ug1 = UG('Matt Damon', 2017)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)

six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

print()

print(gradeReport(six00))
'''              

