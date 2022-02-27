"""
Included here: Day 5 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

#practice with while loops
#While loops, check condition then execute block


def PracticeWhileLoop(x):
    print('EXECUTING WHILE LOOP')
    while x < 5:
        print(f'The value of x is {x}')
        #x = x + 1
        x += 1
PracticeWhileLoop(0)

#Do-While loops (dont exist in python so we change a while loop), 
#execute the block then check condition 
def PracticeDoWhileLoop(x):
    print('EXECUTING DO-WHILE LOOP')
    while True:
        print(f'The value of x is {x}')
        #x = x + 1
        x += 1
        if x >= 5:
            break
print()
PracticeDoWhileLoop(0)

def PracticeForLoop(x):
    if x < 0:
        inc = -1
    else:
        inc = 1
    print('EXECUTING FOR LOOP')
    for i in range(0,x,inc):
        print(f'The value of x is {i}')

print()
PracticeForLoop(20)

#nested for loops are loops within loops
def PracticeNestedForLoop(n):
    print('EXECUTING FOR LOOP WITH NESTED FOR LOOP')
    for x in range (0,n+1):
        for y in range(0,n+1): #the nested for loop
            print(f'(x,y) = ({x},{y})')

print()
PracticeNestedForLoop(5)