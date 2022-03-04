"""
Included here: Day 10 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

def Decimal2Binary(num): 
    def innerAlg(num):
    #base case
        if num == 1:
            return str(num % 2)
        #recursive case
        mod = num % 2
        div = num // 2
        return str(innerAlg(div)) + str(mod)
    def innerFormat(string):
        bits = len(string)
        count = 16 - bits
        leadingZero = count * '0'
        return leadingZero + string
    str1 = innerAlg(num)
    return innerFormat(str1)
    
DecimalNumber = 55    
print(f'{DecimalNumber} as a 16-bit binary number is:',Decimal2Binary(DecimalNumber))
BinStr = Decimal2Binary(DecimalNumber)
BinStr = BinStr.split('0')
BinCount = max([len(num) for num in BinStr if num != ''])
print(BinCount)