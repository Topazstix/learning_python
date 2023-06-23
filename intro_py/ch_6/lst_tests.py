#!/usr/bin/env python3

## MODULE IMPORT
import random #random.randrange(1,10)

## FUNCTIONS

## getNumber() function for setting the user input of items per list
#
def getNumber(): # THIS TAKES USER INPUT ON THE AMOUNT OF VARIABLES PER LIST
    getNum=int(input("How many numbers per list: "))
    return getNum
    
    
## generateList(getNum) function to generate a random list of numbers between 1 and 10
# @param getNum user input variable for items per list
#
def generateList(getNum):
    randomlist = []
    for i in range(getNum):
        n = random.randrange(1,10)
        randomlist.append(n)
        return(randomlist[i])

## addLists(getNum,list_1,list_2,added_List) function to add each index from two lists together and save it to another list
# @param getNum user input variable for items per list
# @param list_1 first randomly generated list
# @param list_2 second randomly generated list
# @param added_List list from adding list_1[i] + list_2[i]
#
def addLists(getNum,list_1,list_2,added_List): # list 1[x] + list 2[x]
    x=0
    while x < getNum :
        added_List.append(list_1[x] + list_2[x])
        x = x + 1
    return added_List

    
    

## multiplyLists(getNum,list_1,list_2,multiplied_List) 
# @param getNum user input variable for items per list
# @param list_1 first randomly generated list
# @param list_2 second randomly generated list
# @param multiplied_List list from multiplying list_1[i] * list_2[i]
#
def multiplyLists(getNum,list_1,list_2,multiplied_List): 
    x=0
    while x < getNum :
        multiplied_List.append(list_1[x] * list_2[x])
        x = x + 1
    return multiplied_List
    
## displayList(prompt,lst)
# @param prompt is the beginning column of the table to be printed, IE "List 1: "
# @param lst is the list stored in main to be printed and formatted
#
def displayList(prompt,lst):
    print("%20s" % prompt, end=' ')
    print("%-20s" % ' '.join([str(x) for x in lst]))

## main() Controls the flow of the rest of the functions contained
#
def main(): 
    
    list_1=[]
    list_2=[]
    added_List=[]
    multiplied_List=[]
    getNum=getNumber()
    for x in range(getNum):
        list_1.append(generateList(getNum))
    for x in range(getNum):
        list_2.append(generateList(getNum))
    added_List=addLists(getNum,list_1,list_2,added_List)
    multiplied_List=multiplyLists(getNum,list_1,list_2,multiplied_List)
    displayList("List 1: ", list_1)
    displayList("List 2: ", list_2)
    displayList("Added List: ", added_List)
    displayList("Multiplied List: ", multiplied_List)
    


## EXECUTION
main()

