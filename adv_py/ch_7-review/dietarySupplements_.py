#!/usr/bin/env python3


## index(list, vitaminName) function used to return the 
## index of a vitamin's name on the list
# @param lst is the list used for determining vitamins 
# @param vitaminName is the actual supplements name
#
def index(lst, vitaminName) : 
    for i in range(len(lst)): 
        if lst[i][0] == vitaminName:
            # Found Vitamin
            return i
    # Did not find vitamin
    return -1 

## getData(filename) function used for opening text file and returning 
## each line of the file as a list of tuples stored as (Vitamin, Amount)
# @param filename is the actual name of the text file used to open
#
def getData(filename) : 
    file = open(filename, "r")
    supplementList = []
    
    # Looping every line in the file
    for line in file : 
        # Separate lines by commas
        data = line.strip().split(",")
        # Add to the list as a tuple containing both vitamin name and amount
        supplementList.append((data[0].strip(), float(data[1])))
    file.close()
    #DEBUG
#    print(supplementList)
    return supplementList

## printSupplements(fmList, mList) is a function used to print human readable
## format with the differences in vitamins and amounts from two lists
# @param fmList is the female supplements list
# @param mList is the male supplements list
#
def printSupplements(fmList, mList) :
    
    # Print the header for the list
    print("Supplement Differences")
    print("%-24s %-24s %-24s" % ("Female", "Male" , "Larger Difference"))
    print("%-24s %-24s %-24s" % ("-" * 24, "-" * 24 , "-" * 24))
    
    # Loop for going thru each (vitamin,value) in the female tuples
    for vitamin, value in fmList :
        # References male list to see if vitamin exists there
        compare = index(mList, vitamin)
        if compare != -1 : 
            # Setting values for comparison
            female = value
            male = mList[compare][1]
            
            # Checks to see if one value is greater or less than its counterpart. Skips values which are the same
            if female < male :
                print("%-24s %-24s %-24s" % (vitamin + ", " + str(female), vitamin + ", " + str(male), "%8.1f" % (male - female) + " - Male"))
                
            elif female > male :
                print("%-24s %-24s %-24s" % (vitamin + ", " + str(female), vitamin + ", " + str(male), "%8.1f" % (female - male) + " - Female"))
        # If item does not exist on male list, prints not listed
        elif compare == -1 : 
            print("%-24s %-24s %-24s" % (vitamin + ", " + str(value), "Not Listed", "%8.1f %-24s" % (value , " - Female") ))
    
    # Prints values in male list that are not present in female        
    for vitamin, value in mList : 
        compare = index(fmList, vitamin)
        if compare == -1 : 
            print("%-24s %-24s %-24s" % ("Not Listed", vitamin + ", " + str(value), "%8.1f %-24s" % (value , " - Male")  ))

## Execute code
#
if __name__ == "__main__" :
    femaleSupplements = getData("femaleSupplement.txt")
    maleSupplements = getData("maleSupplement.txt")
    printSupplements(femaleSupplements, maleSupplements)

#DEBUG
# print(getData("femaleSupplement.txt"))
# print(getData("maleSupplement.txt"))
