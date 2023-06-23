##
# This file tests the person class


from person import Person

p = Person()

flag = True
while flag : 
    print("\n" + "-------" *5 + "\n")
    print("\n" + "-------" *5 + "\n")
    fullName = input("Enter a full name with middle init name: ")
    p.setName(fullName)
    p.getName()
    print(p.getName())
    print("\n" + "-------" *5 + "\n")
    first = input("Enter a users First Name: ")
    p.setFirstName(first)
    middle = input("Enter a users middle init: ")
    p.setMiddleInit(middle)
    last = input("Enter a users last name: ")
    p.setLastName(last)
    dob = input("Enter a users DOB [MO/DA/YEAR]: ")
    p.setDOB(dob)
    print(p.getFullName())
    print(p.getDOB())
    print(p)
    flagger = input("Would you like to record another record? [yes/no]: ")
    if flagger == 'yes' :
        flag = True
    elif flagger == 'no' :
        flag = False
