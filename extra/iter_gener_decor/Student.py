# !/usr/bin/python3

# Import
from person import Person

## Student subclass of Person
class Student(Person):
    
    def __init__(self):
        self._major= None
    
    @property
    def major(self):
        return self._major    
    
    @major.setter
    def major(self,major):
        self._major= major
        
    @major.deleter
    def major(self) : 
        self._major = None
        
    def __repr__(self):
        return super(Student,self).__repr__() + " Major: " + self.major
