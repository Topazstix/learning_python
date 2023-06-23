# !/usr/bin/python3

# Fibonacci class
class Fibonacci : 
    
    #Constructor
    def __init__(self, range) : 
        self.range = range 
        
    def __iter__(self) : 
        self.first = 0
        self.second = 1
        return self
    
    def __next__(self) : 
        nextNum = self.first
        if nextNum > self.first :
            raise StopIteration
        
        self.first, self.second = self.second, self.first + self.second
        
        return nextNum