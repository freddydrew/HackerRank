"""
Included here: Days 5 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

#practice with while loops
from re import X

#While loops, check condition then execute block
def PracticeWhileLoop(x):
    while x < 5:
        print(f'The value of x is {x}')
        #x = x + 1
        x += 1
PracticeWhileLoop(0)

#Do-While loops (dont exist in python so we change a while loop), 
#execute the block then check condition 
def PracticeDoWhileLoop(x):
    while True:
        print(f'The value of x is {x}')
        #x = x + 1
        x += 1
        if x >= 5:
            break
print()
PracticeDoWhileLoop(0)