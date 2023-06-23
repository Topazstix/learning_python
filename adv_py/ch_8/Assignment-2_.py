#!/usr/bin/env python3


# Main function
if __name__ == "__main__" :
    
    # Opens and stores file in variable and closes file when finished
    textFile = open("words2.txt", "r")
    words = textFile.readlines()
    textFile.close()
    
    
    # Creates empty dictionary 
    dictionary = dict()
    
    # Create a looping set/dictionary containing as keys the first letter of each word and the set being the value 
    # // used to define if a letter isnt used in the words // uses ascii codes to set lower case a-z dict keys
    for i in range(97,123) : 
        dictionary[chr(i)] = set()
        
        #DEBUG
        # print(dictionary)
    
    # Converts all values to lowercase and removes newline from each line. Adds all characters to values with specified keys
    for word in words : 
        word = word.lower().rstrip("\n")
        key = word[0]
        dictionary[key].add(word)
        
        #DEBUG
        # print(dictionary)
    
    # Reads if dictionary is empty (if = set()) and as long as there are values, prints the data sorted alphabetically    
    for key in dictionary.keys() : 
        if dictionary[key] != set() :
            
            # Print the sorted dictionary 
            print(key,sorted(dictionary[key]))
            