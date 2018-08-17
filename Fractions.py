class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)
    
    def getNumer(self):
        return self.numer
    
    def getDenom(self):
        return self.denom
    
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() + self.getDenom() * other.getNumer()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew)
    
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() - self.getDenom() * other.getNumer()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew)
    
    def convert(self):
        return self.getNumer() / self.getDenom()
    
oneHalf = fraction(1,2)
twoThirds = fraction(2,3)