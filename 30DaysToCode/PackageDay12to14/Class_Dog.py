"""
Dog Class (A Sub-Class)
Included here: Day 12, 13 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

from Class_Animal import Animal

class Dog(Animal):
    def __init__(self, age = 1): #init method only gets self in declaration, does not get typed into super()__inti__ call
        super().__init__(age)
        print("A Dog has been created!")

    def Ruff(self):
        print('The dog says ruff!!!')

    def Run(self):
        print("A dog is running!")

    def Eat(self):
        print('A dog is eating!')

    def GetAge(self):
        return self.age

    def Sleep(self):
        print('A dog is sleeping.')
