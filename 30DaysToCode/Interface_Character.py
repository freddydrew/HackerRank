"""
Character Interface
Included here: Day 19 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

from abc import ABC, abstractmethod

class Character(ABC):

    #this is a read-only property, final and static 
    @property
    def base(self):
        return "Character"

    @abstractmethod
    def Attack(self):
        pass

    @abstractmethod
    def Heal(self):
        pass


