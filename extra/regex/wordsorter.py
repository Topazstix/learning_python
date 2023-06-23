#!/usr/bin/python3

# IMPORT 
import re

# Class WordSorter: used for taking a file with text and removing words that end in "ed" or "ing" then sorts the new list
class WordSorter:
    
    # Method used to read the contents of a file into a variable
    def readFile(self, fileName):
        
        words = []
        file = open(fileName, "r")
        inputFile = file.readlines()
        
        for line in inputFile : 
            line = line.strip()
            words.append(line)
        file.close()
        return words
    
    # Method to look at the newly created word list, remove any words that are duplicates, and remove any words ending in "ing" and "ed". The new list is removed and returned as a sorted dictionary 
    def processWords(self, words) : 
        
        processedOutput = dict()
        
        for word in words : 
            if not (re.search(r"ing$", word) or re.search(r"ed$", word)) : 
                if word not in processedOutput : 
                    processedOutput[word] = word
        return sorted(processedOutput)
    
    # Method to take the new dictionary and write its contents to a new file "fileName"
    def writeOutputToFile(self, data, fileName) : 
        
        file = open(fileName, "w")
        
        for word in data : 
            file.write(word + "\n")
        file.close()
            
            
