#!/usr/bin/env python3



## MODULE IMPORT
import random #random.randrange(1,10)

## VARIABLES


## FUNCTIONS

## main() Controls the flow of the rest of the functions contained
#
#
def main(): # THIS IS GOING TO CALL ALL OTHER FUNCTIONS, in order of generating random lists first, with user input 
    
    list_1=[]
    list_2=[]
    added_List=[]
    multiplied_List=[]
    getNum=getNumber()
    for x in range(getNum):
        list_1.append(generateList(getNum))
    for x in range(getNum):
        list_2.append(generateList(getNum))
    added_List.append(addLists(getNum,list_1,list_2,added_List))
    multiplied_List.append(multiplyLists(getNum,list_1,list_2,multiplied_List))
    # displayList(getNum,list_1,list_2,added_List,multiplied_List)
    displayList("List 1: ", list_1)
    
    

##
#
#
def getNumber(): # THIS TAKES USER INPUT ON THE AMOUNT OF VARIABLES PER LIST
    getNum=int(input("Enter the amount of items per list: "))
    return getNum
    
    
## generateList(getNum)
#
#
def generateList(getNum):
    randomlist = []
    for i in range(getNum):
        n = random.randrange(1,10)
        randomlist.append(n)
        return(randomlist[i])

## addLists(getNum,list_1,list_2,added_List)
# @param
# @param
# @param
# @param
def addLists(getNum,list_1,list_2,added_List): # list 1[x] + list 2[x]
    x=0
    while x < getNum :
        added_List.append(list_1[x] + list_2[x])
        x = x + 1
    return added_List

    
    

##
#
#
def multiplyLists(getNum,list_1,list_2,multiplied_List): 
    x=0
    while x < getNum :
        multiplied_List.append(list_1[x] * list_2[x])
        x = x + 1
    return multiplied_List
    
##
#
#
def displayList(prompt,getNum,list_1,list_2,added_List,multiplied_List):
    for x in range(getNum):
        print("%5d" % list_1[x], end='')
    print("")
    for x in range(getNum):
        print("%5d" % list_2[x], end='')
    print("")
    for x in range(getNum):
        print("%5d" % added_List[x], end='')
    print("")
    for x in range(getNum):
        print("%5d" % multiplied_List[x], end='')


## EXECUTION
main()

