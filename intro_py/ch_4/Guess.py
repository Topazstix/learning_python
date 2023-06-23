#!/usr/bin/env python3

# Random Number Guessing Game
import random

# Restart the game function
def restart_game():
    restart=input("Would you like to play again? [Enter yes or no]: ")
    while restart == "yes":
        guessing_game()
    else:
        exit()

# Guessing time function (this is the game)
def guessing_game():
    randNumber=random.randrange(1,100)
    # USED FOR DEBUGGING THE SCRIPT TO ENSURE CLASSES FUNCTION ACCURATELY
    #print("Script running game loop")
    #print(randNumber)
    userGuess = int(input("Enter a number between 1 and 100: "))

    while userGuess != randNumber:
        if userGuess > randNumber:
            print("Your guess is too high.")
            userGuess = int(input("Enter a number between 1 and 100: "))
        elif userGuess < randNumber:
            print("Your guess is too low.")
            userGuess = int(input("Enter a number between 1 and 100: "))
    while userGuess == randNumber:
        print("Congratulations - you are right!")
        restart_game()
        break

# User input to start game
def main():    
    gameStart=input("Would you like to play a guessing game? ")
    while gameStart == 'yes':
        guessing_game()
    else:
        exit()

# Execute main
main()

