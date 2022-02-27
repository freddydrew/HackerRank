"""
Included here: Day 7 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

import array as arr
import numpy as np
import random

#Note: lists in python != arrrays in python.
Example1 = [0, 1, 2, 3, 4] #needs commas, list of integers.
Example2 = ['bob', 'sally', 'jim'] #lists of strings.
Example3 = ['tom', 5, 420.69, False] #lists of mixed data types.

#from array module, must be of FIXED TYPE, i denotes type is integer.
ExampleArr1 = arr.array('i',[3, 6, 9, 12]) 

#from numpy package, more or less like a list, can have multiple types.
#arrays need to be decalred, lists dont, arrays store data compactly and are good\
#for numerical operations
ExampleNp1 = np.array([3, 6, 9, 12])

#CANT do this with lists or Arr arrays (to my knowledge as of 2/27/22)
print('Divide Example Numpy array by 3 =',ExampleNp1/3)

##### Stuff from the DAY 7 Video: Arrays! #####

IntArray1 = np.array([]) #empty array
IntArray2 = np.zeros(4,dtype=int) #array of zero with 1 row and 4 columns
IntArray3 = np.array([5, 2, 9, 1, 3])

#string array 
ShoppingList = np.array(['bananas', 'apples', 'pairs'])

#show what we made
print('IntArray2 =',IntArray2)
print('IntArray3 =',IntArray3)

#change some of the elements
ForChangingElements = np.array([10, 8, 5, 10])
for i in range(0,len(IntArray2)):
    IntArray2[i] = ForChangingElements[i]
print('IntArray2 after changing elements =',IntArray2)

#where method returns 1, 2 object with index and type respectively\
#thats why i index [0][0] to just get the number, then add 1 so the print starts at 1
print('********************* \nMy shopping list:')
count = 0
for idx in ShoppingList:
    print(f'{np.where(ShoppingList == idx)[0][0]+1}.',idx)
print('*********************')

#retrieving objects
print('IntArray3\'s 0th element =',IntArray3[0])

#Sorted array
IntArray3Sort = np.sort(IntArray3)
print('IntArray3Sorted Ascending=',IntArray3Sort)
print('IntArray3Sorted Descending=',IntArray3Sort[::-1])
print('IntArray3 =',IntArray3)

#Random value from array
RandIdx = random.randint(0,100) % len(IntArray3)
print('IntArray3 Indexed randomly =',IntArray3[RandIdx])
