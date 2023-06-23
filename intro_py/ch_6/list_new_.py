#!/usr/bin/env python3

## Module Imports
import random

## Functions

def generateList(getNum) : 
    randomlist = []
    for i in range(getNum):
        n = random.randrange(1,10)
        randomlist.append(n)
        return(randomlist[i])

def getNumber() : 
    getNum = int(input("How many numbers per list: "))
    return getNum

def addLists(list_1,list_2) : 
    return [i + j for i, j in zip(list_1,list_2)]

def multiplyLists(list_1,list_2) : 
    return [i * j for i, j in zip(list_1,list_2)]

def displayList(prompt, l) : 
    print("%20s" % prompt, end='')
    print("%-15s" % ' '.join([str(x) for x in l]))
    
def main() : 
    getNum = getNumber()
    list_1 = generateList(getNum)
    list_2 = generateList(getNum)
    displayList('List 1: ', "%5s" % list_1)
    displayList('List 2: ', "%5s" % list_2)
    displayList('Added List: ', "%5s" % addLists(list_1,list_2))
    displayList('Multiplied List: ', "%5s" % multiplyLists(list_1,list_2))
    
## Execute
main()