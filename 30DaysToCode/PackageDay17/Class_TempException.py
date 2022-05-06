"""
Temperature Exception
Included here: Day 17 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""
from abc import ABC, abstractmethod

class TempException(ABC):

    def __init__(self,temp):
        self.temp = temp
        print('A hot beverage has appeared!')

    @abstractmethod
    def TooHotException(self):
        pass

    @abstractmethod
    def TooColdException(self):
        pass

    @classmethod
    def IsGoodTemp(cls,temp):
        if temp <= 185 and temp >= 160:
            print(f'{temp} is a solid temperature for a hot beverage.')


