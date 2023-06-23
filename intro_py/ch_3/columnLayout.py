#!/usr/bin/env python3

#declare variables
total = 0     #total of all entered tests

#instructions
print("Enter 5 test names, then scores")
#First row
column1Row1 = input("Enter Test Name: ")
column2Row1 = float(input("Score: "))
total = total + column2Row1

#second row
column1Row2 = input("Enter Test Name: ")
column2Row2 = float(input("Score: "))
total = total + column2Row2

#third row
column1Row3 = input("Enter Test Name: ")
column2Row3 = float(input("Score: "))
total = total + column2Row3

#fourth row
column1Row4 = input("Enter Test Name: ")
column2Row4 = float(input("Score: "))
total = total + column2Row4

#fifth row
column1Row5 = input("Enter Test Name: ")
column2Row5 = float(input("Score: "))
total = total + column2Row5

#output totals
print("")
print("Output of Test Scores")
print("---------------------")
print("123456789012123456789") # a count line to show size of each column
print("%-12s %8.2f" % (column1Row1, column2Row1))
print("%-12s %8.2f" % (column1Row2, column2Row2))
print("%-12s %8.2f" % (column1Row3, column2Row3))
print("%-12s %8.2f" % (column1Row4, column2Row4))
print("%-12s %8.2f" % (column1Row5, column2Row5))
#print("%-12s %8.2f" % (column1Row5, column2Row5)) #repeat column
print("%-12s %8s" % ("", "--------"))
print("%-12s %8.2f" % ("Total", total))
print("%-12s %8.2f%%" % ("Average", total/5))
