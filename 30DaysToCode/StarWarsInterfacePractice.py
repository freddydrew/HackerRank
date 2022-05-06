"""
Star Wars Interface Practice
Included here: Day 19 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

from Interface_Character import Character


class Hero(Character):

    def __init__(self,name) -> None:
        self.name = name

    def Attack(self):
        return 'He attacks with a lightsaber!'

    def Heal(self):
        return 'He heals himself with the force!'

class Enemy(Character):

    def __init__(self,name) -> None:
            self.name = name

    def Attack(self):
        return 'He attacks but misses!'

    def Heal(self):
        return 'He heals himself with meds.'




Luke = Hero('Luke')
DarthVader = Enemy('Darth Vader')
ObiWanKenobi = Hero('Old man Ben Kenobi')
StormTrooper = Enemy('Storm Trooper')

#read-only, not from a constructor but made like a method with property decorator
print(Luke.base) #can see the property and call it like an attribute
