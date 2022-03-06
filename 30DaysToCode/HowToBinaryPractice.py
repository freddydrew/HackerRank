"""
Included here: Day 10 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

#func that converts decimal to binary, returns string of bits, only works for <= 16-bit numbers
def Decimal2Binary(num): 
    def innerAlg(num):
    #base case
        if num == 1: #last step has a dividend of 1
            return str(num % 2) #last steps bit is the left-most bit overall
        #recursive case
        remain = num % 2 #becomes bit for this step of the conversion
        #integer division here to get the dividend for the next step
        dividend = num // 2 #becomes dividend of next step, divisor of 2 always
        return str(innerAlg(dividend)) + str(remain) #bit from first step is the right-most bit

    #this function combines the output from before with leading zeros to represent the binary 
    #number as a 16-bit or 2-byte number
    def innerFormat(string):
        bits = len(string) #number of bits from conversion to binary
        count = 16 - bits #finding number of needed leading zeros
        leadingZero = count * '0' #creating string to horizontally cat to binary number
        return leadingZero + string #returning the 16-bit number
    str1 = innerAlg(num) #calling the conversion scripts
    return innerFormat(str1) #returning the converted number, in binary, as a string
    
DecimalNumber = 55 #number to convert to binary   
print(f'{DecimalNumber} as a 16-bit binary number is:',Decimal2Binary(DecimalNumber))

#Part of the Day 10 Coding Challenge, supposed to convert number then provide 
#the largest grouping of consecutive bits that are equal to 1
BinStr = Decimal2Binary(DecimalNumber)
BinaryNumber = BinStr
BinStr = BinStr.split('0') #splits up the string at the zeros, reults in the groupings of 1's and empty elements
#where the zeros once were

#iterate through the string array, take only the elements that are not empty, find the length of each element,
#find the element with the largest length, return that as the largest grouping of consecutive ones in the binary number.
BinCount = max([len(num) for num in BinStr if num != ''])
print(f'The largest grouping of consecutive ones in the binary representation of {DecimalNumber} is:',BinCount)

def Binary2Decimal(num):
    #base cases
    if len(num) == 1 and num == str(1): #if the right most bit is 1, raise it tot he zero power
        return 2**0
    if len(num) == 1 and num != str(1): #if the right most bit is zero, pass back a zero for the summation of converted bits
        return 0

    #recursive cases
    bitlen = len(num) - 1 #get the exponent of the 2 for this bit
    current_bit = num[0] #keep the current bit to see if it'll become 0 or 2 raised to the exponent 
    num = num[1::]  #only pass the following right bits to the next step of the recursion
    if current_bit == str(1): #if the current bit is one, raise it to the exponent and got to the next recursion step
        return int(Binary2Decimal(num)) + 2**bitlen
    return int(Binary2Decimal(num)) + 0 #if the current bit is zero, make the conversion 0 and go to the next step of recursion 

print(f'The binary number {BinaryNumber} represented in decimal is:',Binary2Decimal(BinaryNumber))