# !/usr/bin/python3

class FibSeq:
    
    def __init__(self, length):
        
        self.length = length
        self.counter = 0
  
    def __iter__(self):
        
        self.num1 = 0
        self.num2 = 1
        
        return self

    def __next__(self):

        if self.counter > self.length:

            raise StopIteration

        else:
            
            nextNum = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.counter += 1

        return nextNum
    
# from FibSeq import FibSeq

length = int(input("What length would you like? "))

f = FibSeq(length)
f.__iter__()

for i in range(length):

    print(f.__next__())

    i += 1