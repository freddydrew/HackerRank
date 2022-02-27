"""
Included here: Day 3 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""
#would be good to get familiar with these, 
#to know the useful methods from each
import random #for the random function

#Simulating a Coin Toss 
def TossOfCoin():
    #randmom number generation! 
    #abs and round are built in functions
    #picks a random float number, rounds it to the nearest int,   
    #finds the absolute value, mods it to get 0 or 1
    toss = abs(round(random.random())) % 2 
    if toss == 0: #evens are heads, odds are tails
        return 'Heads!'
    return 'Tails!'

#print the result of calling TossOfCoin
print('Heads or Tails?',TossOfCoin())