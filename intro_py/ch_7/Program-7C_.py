#!/usr/bin/env python3

# Import modules
import os
from os import path

## is_file_empty(file_path) function for determining whether a file path exists and whether
## the file specified is empty
# @param file_path is the path of a file on the local machine
#
def is_file_empty(file_path):
    # Check if file exist and it is empty
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0

# Clause for determining whether an input file exists and how to handle it
done = False
while not done : 
    try :
        inputFileName =  input('Enter Input file name (or enter quit to exit): ')
        if path.isfile(inputFileName) : 
            if is_file_empty(inputFileName) == True:
                raise IOError
            elif is_file_empty(inputFileName) == False :
                done = True
        elif inputFileName == "quit" : 
            print("Quitting program")
            quit()
        elif path.isfile(inputFileName) == False : 
            raise FileNotFoundError
    # Handles error for file not found
    except FileNotFoundError : 
        print("File does not exist. ")
    # Handles error for file empty
    except IOError : 
        print("Input file is empty. ")

# Create file to output to
outputFileName =  input('Enter Output file name: ')

# Opens input/output files
try : 
    inputFile = open(inputFileName, "r")
    outputFile = open(outputFileName, "w")
    total = 0
    # Prints lines from input file with numbers and formatted in output file
    for line in inputFile:
        total = total +1
        outputFile.write("/* %d */ %s"%(total,line))
finally : 
    inputFile.close()
    outputFile.close()