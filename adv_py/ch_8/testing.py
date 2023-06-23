def main():
    uniqueWords = set()
    
    filename = input("Enter filename (default: words2.txt): ")
    if len(filename) == 0 :
        filename = "words2.txt"
    inputFile = open(filename, "r")
    
    for line in inputFile : 
        theWords = line.split()
        for word in theWords :
            cleaned = clean(word)
            if cleaned != "" : 
                uniqueWords.add(cleaned)
                
    print("The document contains", len(uniqueWords), "unique words. ")
    
def clean(string) : 
    result = ""
    for char in string : 
        if char.isalpha() :
            result = result + char.lower()
    return result
main()