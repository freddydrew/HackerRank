"""
Included here: Day 9 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

#Summation of 5 --> 5+4+3+2+1+0
def Summation(n):
    #THE BASE CASE (WE"RE AT THE END)
    if n <= 0:
        return 0 #additive identity property
    #THE RECURSIVE CASE (REPEAT THE ALGORITHM)
    return n + Summation(n-1)

addy = 32
print(f'The Summation of {addy} is:',Summation(addy))

#Factorial of 5 (5!) --> 5*4*3*2*1
def Factorial(n):
    #Base Case
    if n == 1:
        return 1 #multiplicative identity property
    #Recursive Case
    return n * Factorial(n-1)
fact = 4
print(f'The Factorial of {fact} is:',Factorial(fact))

#5**3 --> 5*5*5
def Exponentiation(n,e):
    #base case
    if e == 0:
        return 1
    #recursive case
    return n*Exponentiation(n,e-1)

#e = 0, func = 1
#e = 1, func = 5
#e = 2, func = 25
#e = 3, func = 125
#e = 4, func = 625
#e = 5, func = 3125

base = 2
expo = 8
print(f'{base} raised to {expo} is:',Exponentiation(base,expo))
