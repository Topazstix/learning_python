#!/usr/bin/env python3

# DEFINE CONSTANTS
TIP=8.5
TAX=20
costOfMeal="Cost of meal $"
tax="Tax"
tip="Tip"
total="Total cost $"
amountOwed="Amount owed per person: "

# Get user input
totalNumberPeople=int(input("Enter number of guests: "))
totalMealCost=float(input("Enter cost of meal: "))

# Calculate data from information provided
totalTax=totalMealCost*0.2
totalTip=totalMealCost*0.085
accumulativeTotal=totalMealCost+totalTax+totalTip
pricePerPerson=accumulativeTotal/totalNumberPeople

# Print receipt 
print("")
print("%25s %7.2f" % (costOfMeal,totalMealCost))
print("%23s %9.2f" % (tax,totalTax))
print("%23s %9.2f" % (tip,totalTip))
print("%36s" % ("-------------"))
print("%25s %7.2f" % (total,accumulativeTotal))
print("")
print("%25s $%6.2f" % (amountOwed,pricePerPerson))
