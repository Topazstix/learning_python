
# Import Section
from person import Person
from Student import Student
from Instructor import Instructor

# Demo Person class and testing
# person = Person("testing", "11/11/11")
person = Person()
person.name = "Johnathan Luendowski"
person.DOB = "11/11/11"
# person = property(person.name,person.DOB)

# print(person.name, person.DOB)
print(person)

# print(person.name)
# print(person.DOB)

student = Student()
student.major = "Quack MD"
student.name = "Johnson M Dickson"
student.DOB = "12/12/12"
print(student)

instructor = Instructor()
instructor.name = "Jack Williamson"
instructor.DOB = "911"
instructor.salary = "$25,000.00"
print(instructor)
# print(instructor.salary)



# CURRENTLY BROKEN/ REWORK 
# Demo the student class
# student=Student()
# student.setFirstName("Jimmy")
# student.setMiddleInit("D")
# student.setLastName("Lindenson")
# student.setDOB("06/19/1776")
# student.setMajor("Cyber Security")
# print("Student Information:")
# print(student)

# # Demo the instructor class
# instructor=Instructor()
# instructor.setFirstName("Crosby")
# instructor.setMiddleInit("L")
# instructor.setLastName("Bing")
# instructor.setDOB("04/01/1972")
# instructor.setSalary(56000)
# print("Instructor Information:")
# print(instructor) 
