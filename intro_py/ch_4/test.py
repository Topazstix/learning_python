# def main():
#     result1 = cubeVolume(2)
#     result2 = cubeVolume(10)

#     print("A cube with side length 2 has volume", result1)
#     print("A cube with side length 10 has volume", result2)

# def cubeVolume(sideLength) :
#     volume = sideLength ** 3
#     return volume

# main()
from decimal import Decimal

flag = False
while not flag :
   height = input("Enter number: ")
   if Decimal(height) :
      height = float(height)
      flag = True
   else :
      print("Invalid input")


# cubeVolume(int(input("Enter cube side length: ")))
# converter=input("Enter a number to convert to hex: ")

# fuck=int(converter, base=16)
# print(fuck)

## Box string function

def boxString(contents) :
    n = len(contents) 
    print("-" * (n+2))
    print("!" + contents + "!")
    print("-" * (n+2))
    
boxString("Hello World")

## 
#  This program demonstrates a reusable function.
#  

def main() :
   print("Please enter a time: hours, then minutes.")
   hours = readIntBetween(0, 23)
   minutes = readIntBetween(0, 59)
   print("You entered %d hours and %d minutes." % (hours, minutes))
   
## Prompts a user to enter a value within a given range until the user provides 
#  a valid input.
#  @param low an integer indicating the smallest allowable input
#  @param high an integer indicating the largest allowable input
#  @return the integer value provided by the user (between low and high, 
#  inclusive)   
#
def readIntBetween(low, high) :
   value = int(input("Enter a value between " + str(low) + " and " + 
                     str(high) + ": "))
   while value < low or value > high :
      print("Error: value out of range.")
      value = int(input("Enter a value between " + str(low) + " and " + 
                        str(high) + ": "))
 
   return value    

# Start the program.
main()  




##
#  Simulates the rolling of 5 dice and draws the face of each die in a 
#  graphics window.
#

from ezgraphics import GraphicsWindow
from random import randint

# Define a constant for die size.
DIE_SIZE = 60

def main() :  
   canvas = configureWindow(DIE_SIZE * 7)
   rollDice(canvas, DIE_SIZE)  
   while rollAgain() :
      rollDice(canvas, DIE_SIZE)
      
## Prompt the user whether to roll again or quit.
#  @return True if the user wants to roll again
#

def rollAgain() :
   userInput = input("Press the Enter key to roll again or enter Q to quit: ")
   if userInput.upper() == "Q" : 
      return False
   else :
      return True
  
## Create and configure the graphics window.
#  @param winSize the vertical and horizontal size of the window
#  @return the canvas used for drawing
#

def configureWindow(winSize) :
   win = GraphicsWindow(winSize, winSize)
   canvas = win.canvas()
   canvas.setBackground(0, 128, 0)
   return canvas

## Simulates the rolling of 5 dice and draws the face of each die on a graphical
#  canvas in two rows with 3 dice in the first row and 2 in the second row.
#  @param canvas the graphical canvas on which to draw the dice 
#  @param size an integer indicating the dimensions of a single die
#

def rollDice(canvas, size) :
   # Clear the canvas of all objects.
   canvas.clear()
   
   # Set the initial die offset from the upper-left corner of the canvas. 
   xOffset = size
   yOffset = size
   
   # Roll and draw each of five dice.
   for die in range(5) :
      dieValue = randint(1, 6)
      drawDie(canvas, xOffset, yOffset, size, dieValue)
      if die == 2 :
         xOffset = size * 2
         yOffset = size * 3
      else :
         xOffset = xOffset + size * 2
         
## Draws a single die on the canvas.
#  @param canvas the canvas on which to draw the die
#  @param x the x-coordinate for the upper-left corner of the die
#  @param y the y-coordinate for the upper-left corner of the die
#  @param size an integer indicating the dimensions of the die
#  @param dieValue an integer indicating the number of dots on the die 
#

def drawDie(canvas, x, y, size, dieValue) :
   # The size of the dot and positioning will be based on the size of the die.
   dotSize = size // 5
   offset1 = dotSize // 2 
   offset2 = dotSize // 2 * 4
   offset3 = dotSize // 2 * 7

   # Draw the rectangle for the die.
   canvas.setFill("white")
   canvas.setOutline("black")
   canvas.setLineWidth(2)
   canvas.drawRect(x, y, size, size)

   # Set the color used for the dots.
   canvas.setColor("black")
   canvas.setLineWidth(1)
   
   # Draw the center dot or middle row of dots, if needed.
   if dieValue == 1 or dieValue == 3 or dieValue == 5 :      
      canvas.drawOval(x + offset2, y + offset2, dotSize, dotSize)

   elif dieValue == 6 :
      canvas.drawOval(x + offset1, y + offset2, dotSize, dotSize)
      canvas.drawOval(x + offset3, y + offset2, dotSize, dotSize)

      

   # Draw the upper-left and lower-right dots, if needed.

   if dieValue >= 2 : 
      canvas.drawOval(x + offset1, y + offset1, dotSize, dotSize)
      canvas.drawOval(x + offset3, y + offset3, dotSize, dotSize)

      

   # Draw the lower-left and upper-right dots, if needed.

   if dieValue >= 4 : 
      canvas.drawOval(x + offset1, y + offset3, dotSize, dotSize)
      canvas.drawOval(x + offset3, y + offset1, dotSize, dotSize)      

      

# Start the program.

main()