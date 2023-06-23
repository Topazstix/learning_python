#!/usr/bin/env python3

class Employee : 
     
    def __init__(self, first, last, ID, dept, title) : 
        self.first = first
        self.last = last
        self.id = ID
        self.dept = dept
        self._title = title
    
    @property
    def name(self) : 
        fullName = self.first + " " + self.last
        return fullName
    
    @name.setter
    def name(self, name) : 
        fullName = name.split()
        self.first = fullName[0]
        self.last = fullName[1]

    @property
    def employeeID(self) : 
        return self.id
    
    @employeeID.setter
    def employeeID(self, ID) : 
        self.id = ID

    @property
    def department(self) : 
        return self.dept
    
    @department.setter
    def department(self, dept) : 
        self.dept = dept

    @property
    def title(self) : 
        return self._title
    
    @title.setter
    def title(self, title) : 
        self._title = title
