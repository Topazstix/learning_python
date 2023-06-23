#!/usr/bin/python3

# Import 
from wordsorter import WordSorter

# Instantiate object
process = WordSorter()

# Call all class methods
words = process.readFile("wordEndings.txt")
outputData = process.processWords(words)
process.writeOutputToFile(outputData, "output.txt")
