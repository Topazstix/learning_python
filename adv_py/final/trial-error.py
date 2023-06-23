# Import
# import re

# class Employee : 
     
     
#     def __init__(self, first, last, badge, dept, title) : 
#         # Maybe use? changes format from "first, last" to "first last"
#         # x = name.split()   
#         # self.name1 = x[0]
#         # self.name2 = x[1]
        
#         # Attributes to store        
#         self.first = first
#         self.last = last
#         self.id = badge
#         self.dept = dept
#         self.title = title
        
# # \d for searching for digits
# pattern = re.compile(r'\d\d\d\d\d')
# badgeTest = "12345"
# match = pattern.finditer(badgeTest)

# for match in match : 
#     print(match)


### USE FOR SCRIPT?
# print(len(badge))
# pattern = re.compile(r'\d\d\d\d\d')
# checkBadge = pattern.finditer(badge)
# try: 
#     if len(badge) != 5 : 
#         raise ValueError
#     elif len(badge) == 5 :
#         self.badge = badge
# except ValueError : 
#     test = input("Enter employee ID number in format 12345")

# testLargeString = ''' This
# Is a test
# for multi line string inputs

#  ! @ # $ % ^ & * ( ) + = -  ~ ` 

#  < > ? , . /

# LURKING IN 
# THE SHADOW IS A 
# FUCK TWAT COMING 4 U
# 123-456-789000
# '''

# print(testLargeString)

# # TESTING BULLSHIT
# # name = "John Doe"
# first = "Richie"
# last = "Door"
# badge = "12345"
# dept = "Accounting"
# title = "Manager"

# test = Employee(first, last, badge, dept, title)

# # print(test.name1)
# # print(test.name2)
# print(test.first)
# print(test.last)
# print(test.id)
# print(test.dept)
# print(test.title)

# # # Testing for regex script portion

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
# mo = phoneNumRegex.search("""fuck
#                           777-777-7777
#                           (777)-817-3213""")
# print('Phone number found: ' + mo.group()) 
# print(mo)

# # # FUCK YES THIS RIGHT HERE IS THE RIGHT SHIT :D WOO
# empID = input("Enter employee ID: ")
# if re.search(r"^\d{5}$", empID) : 
#     print("Correct syntax")
# else : 
#     print("Incorrect syntax")
    
# # # COPY/PASTE ME***************************
# name = input("\nEnter the name of the employee: ")
# namePattern = re.search(r"^\w+ \w+$", name)
# try :  
#     if name and namePattern : 
#         if name.split() == IndexError : 
#             raise IndexError
#         else :
#             fullName = name.split()
#             first, last = fullName[0], fullName[1]
#     elif namePattern == None : 
#         raise IndexError
# except IndexError : 
#     clear()
#     print("\nMust enter first and last name only")


# empID = input("Enter the employee ID: ")
# idPattern = re.search(r"^\d{5}$", empID)
# if empID :
#     if  idPattern :
#         empID = int(empID)
#     else :
#         print("\nInvalid ID entry. Enter ID format 12345")
# else : 
#     print("\nField cannot be empty")
    




# ## YAY! Correct code for a regex match on name and splitting
# # Testing section for name regex?
# name = input("\nEnter the name of the employee: ")
# #regex = re.compile(name)
# namesearch = re.search(r"^\w+ \w+$", name)
# print(namesearch)
# if namesearch:
#     print("correct input")
# elif namesearch == None : 
#     print("Invalid name")

# try: 
#     if name : 
#         if name.split() == IndexError : 
#             raise IndexError
#         else :
#             fullName = name.split()
#             first, last = fullName[0], fullName[1]
#     else : 
#         print("\nField cannot be empty\n")
# except IndexError : 
#     print("\nMust enter first and last name only")



# #TESTING FOR PROJECT NINE
# day = input("Enter the day of a month: ")
# month = input("Enter a month's number: ")
# year = input("Enter a year: ")

# # day = int(day)
# # month = int(month)
# # year = int(year)

# print(day,month,year)
# print(type(day))
# print(type(month))
# print(type(year))

# # w = day + 2*month + int(0.6)*month+1 + year + year/4 - year/100 + year/400 +2
# w = int(day) + 2 * int(month) + int(0.6) * int(month) + 1 + int(year) + int(year)/4 - int(year)/100 + int(year)/400 +2

# print(w%7)




# ## TRIAL SHIT FOR READ WRITE 
# from sys import exit

# class Person(object):
#     def __init__(self):
#         self.name = ""
#         self.address = ""
#         self.phone = ""
#         self.age = ""
#         self.whip = {}

#     def writing(self):
#         self.whip[p.name] = p.age, p.address, p.phone
#         target = open('deed.txt', 'a')
#         target.write(str(self.whip))
#         print (self.whip)

#     def reading(self):
#         self.whip = open('deed.txt', 'r').read()
#         name = input("> ")
#         if name in self.whip:
#             print (self.whip[name])

# p = Person()

# while True:
#     print ("Type:\n\t*read to read data base\n\t*write to write to data base\n\t*exit to exit")
#     action = input("\n> ")
#     if "write" in action:
#         p.name = input("Name?\n> ")
#         p.phone = input("Phone Number?\n> ")
#         p.age = input("Age?\n> ")
#         p.address = input("Address?\n>")
#         p.writing()
#     elif "read" in action:
#         p.reading()
#     elif "exit" in action:
#         exit(0)
        
        
        
# ## SAVE OF TRY / EXCEPT BEGINNING OF SCRIPT // copy this back if it doesnt work
# try : 
#     database = "employee_database.txt"
#     dictionary = {}
    
#     if does_file_exist(database) == True : 
#         inputFile = open(database, 'r')
#         for line in inputFile : 
#             idregex = re.compile(r"^\d{5}")
#             mo = idregex.search(line)
#             print(mo.group())            
#             empid = re.search(r"^\d{5}", line)
#             print(empid.group())
#             name = re.search(r"^\w+ \w+", line)
#             print(name.group())
#             print(line)
#             first = line[1]
#             last = line[2]
#             empid = line[0]
#             dept = line[3]
#             title = line[4]
#             addMe = {}
            
            
#             obj = Employee(first, last, empid, dept, title)
#             addMe[empid] = obj
#             dictionary.update(addMe)
            
#         inputFile.close()
#     elif does_file_exist(database) == False : 
#         raise FileNotFoundError

# except FileNotFoundError :
#     print("\nDatabase does not exist, creating now....")
#     outputFile = open(database, "w")
#     outputFile.close()
#     time.sleep(.75)

# # MENU SIX COPY
# def menuSix() : 
#     #Logic to store data to file *** INPUT HUR
#     print("\nSaving dictionary to databse...")
#     print("********************\n")
#     f = open(database, "w")
#     for key in dictionary : 
#         f.write(str(dictionary[key].id))
#         f.write(" ")
#         f.write(str(dictionary[key].name))
#         f.write(" ")
#         f.write(str(dictionary[key].department))
#         f.write(" ")
#         f.write(str(dictionary[key].title))
#         # f.write(str(dictionary))
#         f.write("\n")
#     f.close()
#     time.sleep(.25)
#     # Exit
#     print("\nExiting program...")
#     print("********************\n")
#     time.sleep(.75)
#     clear()
#     sys.exit()
    
    
    
    
import re
    
    
# FINAL BULLSHIT

textsearch = ''' Hello
hello
maybe
finite
ABC123 '''
hello = "Hello"
hello2 = "hello"
maybe = "maybe"
finite = "finite"
abc = "ty"

pattern = re.search(r"[a-g]", abc)
print(pattern)