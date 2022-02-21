"""
Included here: Days 4 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

import random

def HowBigIsMyNumber(num):
    #this function will print how large our number is
    if num >= 0 and num <= 10:
        print('Our number is pretty small.')
    elif num >= 11 and num <= 100:
        print('Our number is pretty big.')
    else:
        print('Our number is out of range.')

#Messing around with our conditions being met 
HowBigIsMyNumber(0)
HowBigIsMyNumber(10)
HowBigIsMyNumber(11)
HowBigIsMyNumber(100)
HowBigIsMyNumber(5)
HowBigIsMyNumber(75)
HowBigIsMyNumber(-1)
HowBigIsMyNumber(105)

###### How to play guess the number ########
#1. Computer picks random number
#2. User guesses
#3. Computer gives clues
#4. We guess until we get it


#this function will return a random number between 0 and the set max value
def GuessTheNumber():
    max = 100
    return random.randint(0,max)

#the number that the user will have to guess
TheeNumber = GuessTheNumber()

def play(num):
    # a loop that wont stop until you get it right!
    while True:
        move = int(input('Enter a number: '))
        if move > num:
            print('Your number is too big.')
        elif move < num:
            print('Your number is too small.')
        else:
            print('YOU GOT IT BRO.')
            #break ends the infinite loop if the condition above is met
            break

#start the game!
play(TheeNumber)