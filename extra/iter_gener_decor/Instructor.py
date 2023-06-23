# !/usr/bin/python3

# Import
from person import Person

## Instructor subclass of Person
class Instructor(Person):
    
    def __init__(self):
        super().__init__()
        self._salary=0
        

    @property
    def salary(self):
        return self._salary    
    
    @salary.setter
    def salary(self,salary):
        self._salary= salary
        
    @salary.deleter
    def salary(self) : 
        self._salary = 0
    
    def __repr__(self):
        return super(Instructor,self).__repr__() + " Salary: " + self.salary
