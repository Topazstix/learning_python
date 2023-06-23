#!/usr/bin/env python3

# Import Modules
import math


## main() This is handles the user input section, taking input for radius and height for certain geometric shapes
## and then calls the respective functions for calculations. There are no parameters to this function
#
def main() : 
    areaFormula = input("Input cone, cylinder or sphere to calculate the volume and surface area: ").lower()
    while areaFormula == 'sphere' :
    ## This is a loop statement allowing the user to input only numbers for calculation.
        flag = False
        while not flag :
            radius=input("Enter radius of sphere in inches: ")
            if radius.isalpha() :
                print("Incorrect, please enter a number.")
            else :
                radius= float(radius)
                sphereVolume(radius)
                sphereSurface(radius)
                flag = True
        break
    while areaFormula == 'cone' :
    ## This is a loop statement allowing the user to input only numbers for calculation.
        flag = False
        while not flag :
            radius=input("Enter radius of cone in inches: ")
            height=input("Enter height of cone in inches: ")
            if radius.isalpha() or height.isalpha() :
                print("Incorrect, please enter a number.")
            else :
                radius = float(radius)
                height = float(height)
                coneVolume(radius, height)
                coneSurface(radius, height)
                flag = True
                
        break
    while areaFormula == 'cylinder' :
    ## This is a loop statement allowing the user to input only numbers for calculation.
        flag = False
        while not flag :
            radius=input("Enter radius of cylinder in inches: ")
            height=input("Enter height of cylinder in inches: ")
            if radius.isalpha() or height.isalpha() :
                print("Incorrect, please enter a number.")
            else :
                height = float(height)
                radius = float(radius)
                cylinderVolume(radius, height)
                cylinderSurface(radius, height)
                flag = True
        break
    
## coneSurface(radius, height) this function is designed to calculate formulas for determining the surface area
## of a cone as well as the slant height of a cone and printing in human readable formats
# @param radius the user given radius of a cone
# @param height the user given height of a cone
#
def coneSurface(radius, height) : 
    # Formula calculating the slant
    slant = math.sqrt(radius ** 2 + height ** 2)
    
    # Formula calculating the surface area
    coneSurface = math.pi * radius * (radius + slant)
    
    # Print human readable format for results
    print('Cone slant height is', '%.4f' %slant)
    print('Cone surface of radius', '%.3f' %radius, 'and height of', '%.3f' %height, 'is', '%.4f' %coneSurface, 'inches squared.')

## coneVolume(radius, height) this is a function for determining the volume of a cone and printing in
## human readable format
# @param radius the user given radius of a cone
# @param height the user given height of a cone
#
def coneVolume(radius, height) : 
    # Formula calculating the volume
    coneVolume = (1.0/3) * math.pi * radius ** 2 * height
    
    # Print human readable format for results
    print('\nCone volume of radius', '%.3f' %radius, 'and height of','%.3f' %height, 'is', '%.4f' %coneVolume, 'inches cubed.')    

## sphereVolume(radius) this function is designed to determine the volume of a sphere and print the results in 
## human readable format
# @param raidus the user given radius of a sphere
# 
def sphereVolume(radius) :
    # Formula calculating the volume
    sphereVolume = (4 / 3) * math.pi * radius ** 3
    
    # Print human readable format for results
    print('\nSphere volume of radius', '%.3f' %radius, 'is', '%.4f' %sphereVolume, 'inches cubed.')
    
## sphereSurface(radius) this function is designed to determine the surface area of a sphere and print the results
## in human readable format
# @param radius the user given radius of a sphere
#
def sphereSurface(radius) :
    # Formula calculating the surface area
    sphereSurface =  4 * math.pi * radius ** 2
    
    # Print human readable format for results
    print('Sphere surface of radius', '%.3f' %radius, 'is', '%.4f' %sphereSurface, 'inches squared.')

## cylinderVolume(radius, height) this is a function designed to determine the volume of a cylinder and print the
## results in human readable format
# @param radius the user given radius of a clyinder
# @param height the user given height of a cylinder
#
def cylinderVolume(radius, height) : 
    # Formula calculating the volume
    cylinderVolume = math.pi * radius ** 2 * height
    
    # Print human readable format for results
    print('\nCylinder volume of radius','%.3f' %radius, 'and height of','%.3f' %height, 'is','%.4f' %cylinderVolume, 'inches cubed.')
    
## cylinderSurface(radius, height) this function is designed to determine the surface area of a cylinder and print
## the results in human readable format
# @param radius the user given radius of a clyinder
# @param height the user given height of a cylinder
#
def cylinderSurface(radius, height) :
    # Formula calculating the surface area
    cylinderSurface = 2 * math.pi * radius * (height + radius)
    
    # Print human readable format for results
    print('Cylinder surface of radius','%.3f' %radius, 'and height of','%.3f' %height, 'is','%.4f' %cylinderSurface, 'inches squared.')
    
    
# Execute the program
main()