"""
Cat Class (A Sub-Class)
Included here: Day 12, 13 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

from Class_Animal import Animal

class Cat(Animal):
    def __init__(self, age = 9): #init method only gets self in declaration, does not get typed into super()__inti__ call
        super().__init__(age)
        print("A Cat has been created!")

    def Meow(self):
        print('The cat says meow!!!')

    def Prance(self):
        print("A cat is prancing!")

    def Eat(self):
        print('A cat is eating!')

    def GetAge(self):
        return self.age   