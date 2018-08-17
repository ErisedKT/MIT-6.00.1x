class Person1(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person1):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person1.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff) 
class ArrogantProfessor(Professor):
    def say(self, stuff):
        return Person1.say(self, 'It is obvious that ') + Person1.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Person1.say(self, stuff)