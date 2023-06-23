#!/usr/bin/env python3



# Import Person class
from person import Person

# Print Header for script
print("-------" *11)
print("This is a script that stores and shows names of people and dates of birth.")
print("If no names are entered default values are used.")
print("-------" *11 + "\n")

# call class as an object
p=Person()


# Function for utilizing every method in the person class
# and displays the data as the information is recorded.
# Quits when "no" entered.
flag = True
while flag : 
    print("\n" + "-------" *5 + "\n")
    p.setFirstName()
    p.setMiddleInit()
    p.setLastName()
    name1 = p.getFullName()
    p.setDOB()
    dob1 = p.getDOB()

    print("\n" + name1 + "\n" + dob1 + "\n")
    print("\n" + "-------" *5)
    print(" " )

    flagger = input("Would you like to record another record? [yes/no]: ")
    if flagger == 'yes' :
        flag = True
    elif flagger == 'no' :
        flag = False
