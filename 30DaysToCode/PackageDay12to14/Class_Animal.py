"""
Animal Class (A Super-Class)
Included here: Day 12, 13 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

#abc = Abstract Base Class
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,age):
        print('An Animal has been created!')
        self.age = age

    @abstractmethod
    def Eat(self):
        pass

    @abstractmethod
    def GetAge(self):
        pass

    #this allows me to use this method without the class being instantiated,
    #which i cant do because this is an abstract class!
    @classmethod
    def Sleep(cls):
        print('An animal is sleeping.')