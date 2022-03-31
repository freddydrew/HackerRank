"""
Exceptions Practice
Included here: Day 16 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

#try - try to do something
#except - handle the error
#else - when there is no error do this block
#finally - block lets you execute coe regardless of previous try/except reults

#try fails case
try:
    0fred = 50
#a specific error catch must come before the "catch al" except block
except NameError:
    print('What is this shit even?')
except:
    print('CoolGuyClass Does not exist bro.')

import numpy as np

#try works case
try:
    myArray = np.array([1, 2, 3, 4, 5], float)
#a specific error catch must come before the "catch al" except block
except NameError:
    print('What is this shit even?')
except:
    print('Code broke bro.')
else:
    print('I made your stupid array.')
finally:
    print('Done with this block!')

#raise an exception, if inside of try statement, raising an exception 
#will set off the except statment and you will not see the raise print!
x = int(input('Gimme a positive integer: '))
if x < 0:
    raise Exception('This is not a positive integer, dumbass')
