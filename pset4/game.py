"""Prompts the user for a level n,
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again. #loop
If the guess is smaller than that integer, the program should output 'Too small!' and prompt the user again.
If the guess is larger than that integer, the program should output 'Too large!' and prompt the user again.
If the guess is the same as that integer, the program should output 'Just right!' and exit.
Convert input to integer"""

import random

#reusable(general) function that takes in user input(str) and checks if its a valid number(positive int)
def get_integer(value):
    #check if input can be formatted into a positive input
    #return the input if valid and None if not
    #parameter called value to check for any string input from guess and level(doesnt need to know where it comes from)
    #2 prompts: prompt for a level(to determined range) and prompt for guess within that range

    try:
        #convert user string input into integer and store in num
        num = int(value)
        if num > 0:
            return num
    except ValueError:
        pass #if conversion fails(neg number or alpha), do nothing and return None
    return None #accepts failure of valid input and stops 

def main():
     #1: Level input
     #while we can prompt user for input(checked above for validity)
    while True:
        level_input = input("Level: ")
        level = get_integer(level_input) #the called output of level input

        if level is not None: #if input is valid(not the valueerror), we move on to random
            break #exit the loop if valid input

    #using random module, generate random number between 1 and level entered and store it in "target"
    target = random.randint(1, level)

    #2:Guess input
    #prompt for user to guess a number (internally randomised) in the level range
    while True:
        guess_input = input("Guess: ")
        guess = get_integer(guess_input)

        #if value is greater than target, print
        if guess is None:
            continue #if theres an invalid guess, continue and reloop for guess

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else: #if its the right guess
            print("Just right!")
            break

if __name__ == "__main__":
    main()






