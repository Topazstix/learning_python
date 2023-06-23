# !/usr/bin/python3

class Person : 
    
    def __init__(self, name=None, dob=None) : 
    # Variables first, middle. last, dob, name
        # self.first = ""
        # self.last = ""
        self._name = name
        self._dob = dob

    @property
    def name(self) : 
        return self._name
    
    @name.setter
    def name(self, name) :
        self._name = name
    
    @name.deleter
    def name(self) : 
        self._name = None

    @property
    def DOB(self) :
        return self._dob
    
    @DOB.setter
    def DOB(self, dob) : 
        self._dob = dob
    
    @DOB.deleter
    def DOB(self) : 
        self._dob = None

    # Added a __repr__ method to person class
    def __repr__(self):
        return "Full Name: " + self.name + " DOB: " + self.DOB




