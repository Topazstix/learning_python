#!/usr/bin/env python3

# Import section
import os
import pickle
import re
import sys
import time

from employee import Employee

# # function to clear screen after menu selection // 
# # doesnt work in idle so this is disabled. looks better with this function however. 
def clear() : 
    if os.name == "nt" :
        _ = os.system("cls")
    else : 
        _ = os.system("clear")

# Logic to check if employee database exists and use pickle to load it into
# a dictionary, else create an empty dictionary
try : 
    database = "employee_database.txt"
    inputFile = open(database, 'rb')
    dictionary = pickle.load(inputFile)
    inputFile.close()
except : 
    dictionary = {}


# main script, handles the menu creation and input validation
def main() : 
    while True :
        # Program Menu
        print('\n1. Look up an employee in the database')
        print("2. Add a new employee to the database")
        print("3. Change an existing employee's name, department and job title in the database")
        print("4. Delete an employee from the database")
        print("5. List all employee records")
        print("6. Quit the program")
        
        # user input
        response = input("\nSelect an option\n> ") 
        time.sleep(.5)
        clear()
        
        # confirms input is digit
        try :
            if response.isdigit() == False :
                raise ValueError
            if response.isdigit() == True :
                response = int(response)
                # if response is higher than available menus
                if response > 6 :
                    clear()
                    print("Invalid entry. Select 1-6")
                    print("********************")
                    continue
                # if response is 0 or other 
                elif response <= 0 :
                    clear()
                    print("Invalid entry. Select 1-6")
                    print("********************")
                    continue
        # handles if letters are input
        except ValueError : 
            clear()
            print("Number was not selected")
            print("********************")
            
        # logic for menu selections
        if response == 1 : 
            menuOne()
        elif response == 2 :
            menuTwo()
        elif response == 3 : 
            menuThree()
        elif response == 4 : 
            menuFour()
        elif response == 5 : 
            menuFive()
        elif response == 6 : 
            menuSix()
        

# Menu one, prints an employees record in formatted columns
def menuOne() : 
    while True : 
        # input employee ID
        empID = input("Enter the employee ID: ")
        # regex pattern to confirm ID in specified format
        idPattern = re.search(r"^\d{5}$", empID)
        try : 
            if empID and idPattern :
                empID = int(empID)
                
                if empID in dictionary : 
                    
                    # retrieve employee from dict
                    obj = dictionary[empID]
                    
                    # print employee record in formatted columns
                    print("-------" * 5 + "-")
                    print("%-10s %20s" % ("\nEmployee Name: ", obj.name))
                    print("%-10s %22s" % ("Employee ID: ", obj.employeeID))
                    print("%-10s %14s" % ("Employee Department: ", obj.department))
                    print("%-10s %15s" % ("Employee Job Title: ", obj.title), "\n")
                    print("-------" * 5 + "-")
                    input("\nPress any key to continue")
                    time.sleep(.75)
                    clear()
                    break
                # if employee not found in dict
                else :
                    clear()
                    print("Employee not in database")
                    print("********************")
                    time.sleep(1)
                    break
            # if ID entered is not in specified format
            elif idPattern == None :
                raise ValueError
        except ValueError :
            clear()
            print("Invalid ID entry. Enter ID format 12345\n")
            continue

# Menu two, adds a new user to the database
def menuTwo() : 
    while True : 
        # get employee name
        name = input("Enter the name of the employee: ")
        # regex pattern confrims input matches exactly two words
        namePattern = re.search(r"^\w+ \w+$", name)
        try :  
            if name and namePattern : 
                # takes input and splits it into two variables for use in employee class
                fullName = name.split()
                first, last = fullName[0], fullName[1]
                break
            # if input is not two words, raise error
            elif namePattern == None : 
                raise IndexError
        # handles input error of less than or more than 2 words
        except IndexError : 
            clear()
            print("Must enter FIRST and LAST name only\n")
            continue
    
    # get employee ID
    while True : 
        empID = input("Enter the employee ID: ")
        # regex pattern to confirm ID in specified format
        idPattern = re.search(r"^\d{5}$", empID)
        try : 
            if empID and idPattern :
                empID = int(empID)
                break
            elif idPattern == None :
                raise ValueError
        except ValueError : 
            print("\nInvalid ID entry. Enter ID format 12345")
            continue
        
    # get employee department
    while True : 
        dept = input("Enter the employee department: ")
        if dept : 
            break 
        else : 
            print("\nField cannot be empty")
            continue
        
    # get employee title
    while True : 
        title = input("Enter the employee job title: ")
        if title :
            break
        else : 
            print("\nField cannot be empty")
            continue
    
    # create employee object
    obj = Employee(first, last, empID, dept, title)
    
    # add object to dictionary
    dictionary[empID] = obj
    print("\nEmployee record created")
    print("********************")
    time.sleep(1)
    clear()

# Menu three, allows user to change the details of an employee in the database
def menuThree() : 
    while True : 
        
        # get employee ID from user
        empID = input("Enter the ID number of the employee to change: ")
        # regex pattern to confirm ID in specified format
        idPattern = re.search(r"^\d{5}$", empID)
        if empID : 
            if  idPattern : 
                empID = int(empID)
                obj = None
                if empID in dictionary : 
                    obj = dictionary[empID]
                    name = dictionary[empID].name
                    print("\nYou are changing the record for", name)
                    # Logic to change the details of employee in database
                    while True : 
                        # get employee name
                        name = input("Enter new name for the employee: ")
                        # regex pattern confrims input matches exactly two words
                        namePattern = re.search(r"^\w+ \w+$", name)
                        if name and namePattern : 
                            obj.name = name
                            break
                        # if pattern doesnt match
                        else : 
                            clear()
                            print("Must enter first and last name only\n")
                            continue

                    while True : 
                        dept = input("Enter new department name: ")
                        if dept : 
                            obj.department = dept
                            break
                        else : 
                            print("\nDepartment field cannot be empty")
                            continue
                    
                    while True : 
                        title = input("Enter new job title for employee: ")
                        if title : 
                            obj.title = title
                            break
                        else : 
                            print("\nTitle field cannot be empty")
                            continue
                    
                    # Continued from if empID in dictionary statement
                    print("\nEmployee database updated successfully")
                    print("********************\n")
                    time.sleep(1)
                    clear()
                    break
                # else if employee ID not found in dictionary
                else : 
                    # ID not found
                    print("\nEmployee ID not found")
                    print("********************\n")
                    time.sleep(1)
                    clear()
                    break
            # else if ID pattern does not match
            else : 
                clear()
                print("Invalid ID entry. Enter ID format 12345\n")
                continue
        # else if field empty
        else : 
            clear()
            print("Empoyee ID field cannot be empty\n")
            continue

# Menu four, deletes an employee from the database
def menuFour() : 
    while True : 
        
        # get employee ID from user
        empID = input("Enter the ID number of the employee to delete: ")
        # regex pattern to confirm ID in specified format
        idPattern = re.search(r"^\d{5}$", empID)
        if empID : 
            if idPattern : 
                empID = int(empID)
                if empID in dictionary : 
                    name = dictionary[empID].name
                    print("\nEmployee name: ", name)
                    choice = input("Are you sure you want to remove this record?[Y or N] ").lower()
                    if choice == "y" : 
                        del dictionary[empID]
                        clear()
                        print("Record has been removed")
                        print("********************\n")
                        time.sleep(1)
                        clear()
                        break
                    else :
                        print("\nRecord has not been removed")
                        print("********************\n")
                        time.sleep(1)
                        clear()
                        break
                # if employee not in dictionary
                else : 
                    print("Record not found")
                    print("********************\n")
                    time.sleep(1)
                    clear()
                    break
            # if pattern does not match
            else : 
                clear()
                print("Invalid ID entry. Enter ID format 12345\n")
                continue
        # if field is empty
        else : 
            clear()
            print("Empoyee ID field cannot be empty\n")
            continue

# Menu five, prints in formatted columns all records in the database, sorted by employee ID
def menuFive() : 
    # Print column header
    print("---------" * 8)
    print("%-10s %20s %22s %16s" % ("Employee ID", "Employee Name", "Department", "Title"))
    print("---------" * 8)
    
    # print all records, format to pretty columns
    for key in sorted(dictionary) : 
        print("%-10s %20s %22s %17s" % (dictionary[key].employeeID, dictionary[key].name, dictionary[key].department, dictionary[key].title))
    # column footer
    print("********" * 9)
    input("\nPress any key to continue")
    clear()

# Menu six, stores pickled dictionary to a database and exits the program
def menuSix() : 
    print("Saving dictionary to databse...")
    print("********************\n")
    # open database file and dump the dictionary via pickle to the file
    try : 
        outputFile = open(database, "wb")
        pickle.dump(dictionary,outputFile)
    finally : 
        outputFile.close()
        time.sleep(.5)
        # Exit
        print("Exiting program...")
        print("********************\n")
        time.sleep(.75)
        clear()
        sys.exit()

# # THIS IS A DEBUG MENU FOR DELETING ALL RECORDS
# def menuSeven() : 
#     input("Press enter to delete all employees from the database")
#     global dictionary 
#     dictionary = None
#     dictionary = {}

# call the script
if __name__ == "__main__" : 
    main()
    
    