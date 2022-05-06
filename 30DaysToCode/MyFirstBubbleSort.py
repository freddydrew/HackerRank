"""
My first Bubble Sort!
Included here: Day 20 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

TestArray = [1, 5, 2, 8, 4, 7, 2, 8, 11, 54, 37]
print('Test array before sorting:', TestArray)

numSwaps = 0
for i in range(0,len(TestArray)):
    for j in range(0,len(TestArray)-1):
        if TestArray[j] < TestArray[j + 1]:
            tmp = TestArray[j]
            TestArray[j] = TestArray[j + 1]
            TestArray[j + 1] = tmp
            numSwaps += 1
            print(f'Test array after swap {numSwaps}:',TestArray )
            
            
            