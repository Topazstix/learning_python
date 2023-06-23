# !/usr/bin/python3

# Import
import unittest
from person import Person
from Student import Student
from Instructor import Instructor

# Create objects
person = Person()
student = Student()
instructor = Instructor()

class TestClasses(unittest.TestCase) :
    
    def test_Equal(self) :
        self.assertEqual(person.DOB, "11/11/11")
        self.assertEqual(instructor.salary, "$45,000.00")
        del person.name
        del person.DOB
        del instructor.salary

    def test_Is(self) : 
        self.assertIs(instructor.salary, int())

    def test_None(self) :  
        self.assertIsNone(person.name)
        self.assertIsNone(student.major)

    def test_Init(self) : 
        self.assertIsNone(person.__init__())
        self.assertIsNone(student.__init__())
        self.assertIsNone(instructor.__init__())

    def test_Instance(self) : 
        self.assertIsInstance(person, Person)
        self.assertIsInstance(student, Student)
        self.assertIsInstance(instructor, Instructor)

if __name__ == "__main__" : 
    person.name = "Jack Johnson"
    person.DOB = "11/11/11"
    instructor.salary = "$45,000.00"
    unittest.main()
