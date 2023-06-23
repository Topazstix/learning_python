#!/usr/bin/env python3
import os
import os.path
from os import path
from pathlib import Path


data_folder = Path("C:\\Users\\\\Documents\\College\\")

done = False
while not done: 
    try : 
        fileName = input("Enter file name to open: ")
        if fileName == "quit" :
            done = True
        else : 
            infile = open(fileName, "r")
            line = infile.readline()
            print(line)

            # done = True
    except IOError : 
        print("Could not open input file.")
    except Exception as exceptObj :
        print("Error:", str(exceptObj))


# done = False
# while not done : 
#     amount = int(input("Enter an amount: "))
#     balance = int(input("Enter a balance: "))
#     try :
#         if amount > balance :
#             raise ValueError("Amount is larger than balance")
#         done = True
#     except ValueError : 
#         print("File not found")
    

# balance = balance - amount