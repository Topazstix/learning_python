
# Import
from person import Person

## Student subclass of Person
class Student(Person):
    
    def __init__(self):
        self._major=""
    
    def setMajor(self,major):
        self._major=major
    
    def getMajor(self):
        return self._major
    
    def __repr__(self):
        return super(Student,self).__repr__() + " Major: " + self.getMajor()
