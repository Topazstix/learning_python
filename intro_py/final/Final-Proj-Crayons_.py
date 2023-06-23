#!/usr/bin/env python3

# Import Modules
import os
from os import path
import sys

# Functions

## is_file_empty(file_path) function for determining whether a file path exists and whether
## the file specified is empty
# @param file_path is the path of a file on the local machine
#
def is_file_empty(file_path) : 
    # Check if file exist and it is empty
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0

## getFilePrevious function for determining what file to open and handling the logic for errors
#
def getFilePrevious() : 
    done = False
    while not done : 
        try:
            fileName = input("Enter the filename for Previous Colors: ")
            if path.isfile(fileName) :
                if is_file_empty(fileName) == True :
                    raise IOError
                elif is_file_empty(fileName) == False : 
                    listPrevious=getData(fileName)
                    return listPrevious
            elif path.isfile(fileName) == False : 
                raise FileNotFoundError
        except FileNotFoundError : 
            print("Error, File not found, exiting program. ")
            sys.exit()
        except IOError : 
            print("File specified is empty.")

## getFileAdded function for determining what file to open and handling the logic for errors
#
def getFileAdded() : 
    done = False
    while not done :
        try:
            fileName = input("Enter the filename for Added Colors: ")
            if path.isfile(fileName) :
                if is_file_empty(fileName) == True :
                    raise IOError
                elif is_file_empty(fileName) == False : 
                    listAdded=getData(fileName)
                    return listAdded
            elif path.isfile(fileName) == False : 
                raise FileNotFoundError
        except FileNotFoundError : 
            print("Error, File not found, exiting program. ")
            sys.exit()
        except IOError : 
            print("File specified is empty.")

## getFileRetired function for determining what file to open and handling the logic for errors
#
def getFileRetired() : 
    done = False
    while not done :
        try:
            fileName = input("Enter the filename for Retired Colors: ")
            if path.isfile(fileName) :
                if is_file_empty(fileName) == True :
                    raise IOError
                elif is_file_empty(fileName) == False : 
                    listRetired=getData(fileName)
                    return listRetired
            elif path.isfile(fileName) == False : 
                raise FileNotFoundError
        except FileNotFoundError : 
            print("Error, File not found, exiting program. ")
            sys.exit()
        except IOError : 
            print("File specified is empty.")

## getData function for opening a specified file and returning the contents in list form
# @Param fileName is the user input name of the file specified to open
#
def getData(fileName) : 
    try : 
        with open(fileName, "r") as f :
            lines = f.read().splitlines()
        return lines
    finally : 
        f.close()

## generateColorList function for operating on multiple lists
# @Param listPre is the previous crayon color list
# @Param listAdd is the added crayon color list
# @Param listRet are the retired colors in list
#    
def generateColorList(listPre,listAdd,listRet) : 
    newList = listPre + listAdd
    adjNewList = [x for x in newList if x not in listRet]
    adjNewList.sort()
    return adjNewList

## displayColorList function for showing the final color list formatted in 2 columns
# @Param colorList is the list of crayon colors after being combined
#    
def displayColorList(colorList) : 
    for idx, key in enumerate(colorList):
        if (idx + 1) % 2:
            print('%30s' % key,  end='\t')
        else:
            print(key, end='\n')

## EXECUTION
if __name__ == "__main__": 

    listPrevious = getFilePrevious()
    listAdded = getFileAdded()
    listRetired = getFileRetired()
    crayonList = generateColorList(listPrevious,listAdded,listRetired)
    displayColorList(crayonList)
