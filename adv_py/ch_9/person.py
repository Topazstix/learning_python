# Class Person, used for recording and storing a persons full name and date of birth
class Person : 
    
    def __init__(self) : 
    # Variables first, middle. last, dob, name
        self._name = ""
        self._dob = ""
        self._first = str()
        self._middle = str()
        self._last = str()

    def setName(self, new_name) :
        self._name = new_name
        
    def setFirstName(self, first) : 
        self._first = first

    def setMiddleInit(self, middle) :
        self._middle = middle
        
    def setLastName(self, last) : 
        self._last = last

    def setDOB(self, dob) : 
        self._dob = dob

    def getDOB(self) :
        return self._dob

    def getName(self) : 
        return self._name

    def getFullName(self) :
        self._name = self._first + " " + self._middle + " " + self._last
        return self._name

    # Added a __repr__ method to person class
    def __repr__(self):
        return "Full Name: {} DOB: {} ".format(self.getFullName(), self.getDOB())
