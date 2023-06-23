
# Import Section
from person import Person
from Student import Student
from Instructor import Instructor


# Demo the student class
student=Student()
student.setFirstName("Jimmy")
student.setMiddleInit("D")
student.setLastName("Lindenson")
student.setDOB("06/19/1776")
student.setMajor("Cyber Security")
print("Student Information:")
print(student)

# Demo the instructor class
instructor=Instructor()
instructor.setFirstName("Crosby")
instructor.setMiddleInit("L")
instructor.setLastName("Bing")
instructor.setDOB("04/01/1972")
instructor.setSalary(56000)
print("Instructor Information:")
print(instructor) 
