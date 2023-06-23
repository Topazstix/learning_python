#!/usr/bin/env python3

## List variables. Values are added thru loops below. 
list_A=[]
list_B=[]
list_C=[]
list_D=[]
list_E=[]
list_F=[]


## List A operations
for i in range(1,10,1):
    list_A.append(i)

# Calculate average value from a given list
averageListA = round(sum(list_A)/len(list_A))    

## List B operations
for i in range(1,12,1):
    powers2 = i ** 2
    list_B.append(powers2)
    
# Calculate average value from a given list
averageListB= round(sum(list_B)/len(list_B))
    
## List C operations
for i in range(0,21,2):
    list_C.append(i)
    
# Calculate average value from a given list
averageListC=round(sum(list_C)/len(list_C))
    
## List D operations
for i in range(25,0,-5):
    list_D.append(i)
    
# Calculate average value from a given list
averageListD=round(sum(list_D)/len(list_D))
    
## List E operations
for i in range(10,32,3):
    list_E.append(i)
    
# Calculate average value from a given list
averageListE=round(sum(list_E)/len(list_E))
    
## List F operations
for i in range(10,-1,-1):
    power3 = i **3
    list_F.append(power3)
    
# Calculate average value from a given list
averageListF=round(sum(list_F)/len(list_F))

# Print statements for list A
print("\nList A: ", list_A)
print("The max value is: ", max(list_A))
print("The min value is: ", min(list_A))
print("The avg value is: ", averageListA)

# Print statements for list B
print("\nList B: ", list_B)
print("The max value is: ", max(list_B))
print("The min value is: ", min(list_B))
print("The avg value is: ", averageListB)

# Print statements for list C
print("\nList C: ", list_C)
print("The max value is: ", max(list_C))
print("The min value is: ", min(list_C))
print("The avg value is: ", averageListC)

# Print statements for list D
print("\nList D: ", list_D)
print("The max value is: ", max(list_D))
print("The min value is: ", min(list_D))
print("The avg value is: ", averageListD)

# Print statements for list E
print("\nList E: ", list_E)
print("The max value is: ", max(list_E))
print("The min value is: ", min(list_E))
print("The avg value is: ", averageListE)

# Print statements for list F
print("\nList F: ", list_F)
print("The max value is: ", max(list_F))
print("The min value is: ", min(list_F))
print("The avg value is: ", averageListF)
