#!/usr/bin/env python3


#Do not change any of my lines of code or variable names!
#Only add the lines necessary to solve the problem
#Do not break this file into individual py files.

import time

#problem 1
#Counter controlled loops (page 85) require three things to work:
# 1. an initialized counter variable      
# 2. a testing of the counter variable
# 3. increment/decrement of the counter variable
#Using variable counter, write a While loop that prints "Programming is FUN!"
#to the screen five (5) times.
print("\nProblem 1\n----------")

counter = 0;
while counter < 5:
    print("Programming is FUN!")
    counter = counter+1      
            
#problem 2
#Now repeat problem 1 using a For...loop and the range() function.
# THIS IS A LINE SEPARATOR
print("\nProblem 2\n----------")
time.sleep(.75)

counter = 0
for counter in range(0,5):
    print("Programming is FUN!")      
      
#problem 3
#Write a For...loop that adds up the numbers 1 to 10 into a total variable.
#print the total to the screen.
# THIS IS A LINE SEPARATOR
print("\nProblem 3\n----------")
time.sleep(.75)

counter=0
total=0
for counter in range(0,10) :
    counter=counter+1
    total+=counter
print(total)

          
#problem 4
#Output the following to the screen using a For...loop and range()function.
# THIS IS A LINE SEPARATOR
print("\nProblem 4\n----------")
time.sleep(.75)

#Counting at 5
#Counting at 4
#Counting at 3
#Counting at 2
#Counting at 1

counter = 6
for counter in range(5,0,-1):
    print("Counting at",counter)

#problem 5
#Using the variable below create a While loop that prints the following
#to the screen:
#2, 4, 6, 8, 10, 12, 14, 16, 18, 20
# THIS IS A LINE SEPARATOR
print("\nProblem 5\n----------")
time.sleep(.75)

counter = 0
while counter != 18 :
    counter=counter+2
    print(counter,", ",sep="",end="")
print(counter+2)

# TEST

      

# THIS IS A LINE SEPARATOR
print("\nProblem 6\n----------")

#problem 6
#Using the following variable, write the code necessary to add the total of all the 
#values from 0 to 100 and print only the total after computing it. You can use
#any loop structure.
# THIS IS A LINE SEPARATOR
time.sleep(.75)

total = 0
counter=0
for counter in range(0,100) :
    counter=counter+1
    total+=counter
print(total)
      
               
#problem 7 
# THIS IS A LINE SEPARATOR
print("\nProblem 7\n----------")
time.sleep(.75)
#Modify problem 6's code to do the same thing, but the maximum number
#(which was 100) should be entered by the user, instead of hardcoding it in
#the loop. So, the user enters a number for the maximum range and all the
#values from 0 to the number entered, which is stored in maxNumber are totaled.

maxNumber = 0
counter=0
max=int(input("Enter range to add through from 0: "))
for counter in range(0,max) :
    counter=counter+1
    maxNumber+=counter
print(maxNumber)
      
#problem 8
#Now modify problem 7 to allow the user to enter the range of numbers to be
#totaled beginning with the min value and the max value.     
#You will need to delcare and initialize variables min and max for use with
#this problem. The keyboard is already declared. You will also
#need to create the prompts and input statements.
# THIS IS A LINE SEPARATOR
print("\nProblem 8\n----------")
time.sleep(.75)

total = 0
counter=0
min=int(input("Enter minimum range to add from: "))
max=int(input("Enter maximum range to add through: "))
for counter in range(min,max) :
    counter=counter+1
    total+=counter
print(total)
      
# THIS IS A LINE SEPARATOR
print("\nProblem 9\n----------")      
time.sleep(.75)

#problem 9
#Write the statements necessary to do the following: Total all the integer
#values a user enters into the computer until they enter -1. Once -1 has
#been entered exit the loop, display the total of the numbers entered. You
#must use a While...loop. Make certain no negative values are added to the
#total. Only exit on -1, not any other negative value.

total = 0
countTotal = int(input("Enter positive integers to count, otherwise enter -1 to quit: "))
while countTotal != -1 :
    total = total + countTotal
    countTotal = int(input("Enter positive integers to count, otherwise enter -1 to quit: "))
    if countTotal < -1 :
        print("You've entered an invalid number. Try Again or enter -1 to quit.")
        total = total - countTotal
print("Your total is", total)
      
#problem 10
#Recreate problem 9, but this time use a flag controlled loop. When the user
#enters a negative value, stop the loop and print the total.
# THIS IS A LINE SEPARATOR
print("\nProblem 10\n----------")     
time.sleep(.75)

total = 0
counter = 0
flag = True
while flag :
    total = total+counter
    counter = int(input("Enter numbers to add together else enter any negative value to quit: "))
    if counter < 0 :
        break
print("Your total is", total)