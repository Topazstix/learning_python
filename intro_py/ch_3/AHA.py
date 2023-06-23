#/usr/bin/env python3

# User inputs
nameOfFood=input("Name of food: ")
caloriesPerServing=int(input("Calories per serving: "))
gramsOfFatPerServing=float(input("Grams of fat per serving: "))

# Calculations
fatCalculation=gramsOfFatPerServing*9
calorieFat=fatCalculation/caloriesPerServing
percentOfFat=calorieFat*100

# Print legible format
print("")
print(nameOfFood, "contains", "%.1f%%" % percentOfFat,"calories from fat." )

if percentOfFat>30 :
    print(nameOfFood,"exceeds the AHA recommendation.")
elif percentOfFat<=30 : 
    print(nameOfFood,"meets the AHA recommendation.")
    
import re 

