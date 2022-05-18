"""
Run Time Practice 
Included here: Day 25 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""
from time import time


#test func to measure speed, O(n)
def FindDupesv1(string,char):
    sum = 0
    for letter in string:
        if letter == char:
            sum += 1
    return sum

#test func to measure speed, O(n*m), quadratic time
def FindDupesv2(string,char): #accepts two strings, iterates through them
    sums = {} #empty frequency table
    for c in char: #O(n)
        for s in string: #O(n) * O(m) --> O(n*m)
            if s in sums and s == c: 
                sums[c] += 1
            if s not in sums and s == c:
                sums[c] = 1
    return sums

#test func to measure speed, O(n+m), linear time
def FindDupesv3(string,char): #accepts two strings, iterates through them
    sums = {} #empty frequency table
    for s in string: #O(n)
        if s not in sums and s in char: #if statments are assumed to be constant time O(1)
                sums[s] = 1
        if s in sums and s in char: #in operator is likely O(m) here
                sums[s] += 1
    return sums



#set my timer!
t1 = time()
#calling func
print('Dupes:',FindDupesv1('frederick','r'))
#clock the porgram!
t2 = time()
dur  = (t2 - t1)
print('Duration:',dur)


#set my timer!
t1 = time()
#calling func
print('Dupes:',FindDupesv2('frederick','red'))
#clock the porgram!
t2 = time()
dur  = (t2 - t1)
print('Duration:',dur)

#set my timer!
t1 = time()
#calling func
print('Dupes:',FindDupesv3('frederick','red'))
#clock the porgram!
t2 = time()
dur  = (t2 - t1)
print('Duration:',dur)