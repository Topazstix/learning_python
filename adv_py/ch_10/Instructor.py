
# Import
from person import Person

## Instructor subclass of Person
class Instructor(Person):
    
    def __init__(self):
        self._salary=0.0
    
    def setSalary(self,salary):
        self._salary=salary
    
    def getSalary(self):
        return self._salary
    
    def __repr__(self):
        return super(Instructor,self).__repr__() + " Salary: " + str(self.getSalary())
