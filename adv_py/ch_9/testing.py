from datetime import date

class Person:

    def __init__(self):

        self.first = ""
        self.mid = ""
        self.last = ""
        self.dob = ""

    def setFirst(self):

        self.first = input("Input your first name: ")

    def getFirst(self):

        return self.first

    def setMid(self):

        self.mid = input("Input your middle initial: ")

    def getMid(self):

        return self.mid

    def setLast(self):

        self.last = input("Input your last name: ")

    def getLast(self):

        return self.Last

    def setDOB(self):

        self.dob = input("Input your date of birth (mm/dd/yyy): ")

    def getDOB(self):

        return self.dob

    def getFullName(self):

        print(self.first + self.mid + self.last)