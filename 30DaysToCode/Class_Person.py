"""
Person Class
Included here: Day 20 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""
from Enum_HairColor import HairColor

class Person:

    def __init__(self,ColorOfHair) -> None:
        self.ColorOfHair = HairColor(ColorOfHair)


#Aliases with spiderman!
PeterParker = Person(3)
SpiderMan = PeterParker

print('Peter\'s hair color',PeterParker.ColorOfHair)
print('Spiderman\'s hair color',SpiderMan.ColorOfHair)

PeterParker.ColorOfHair = HairColor(1)
print('Peter\'s hair color',PeterParker.ColorOfHair)
print('Spiderman\'s hair color',SpiderMan.ColorOfHair)

SpiderMan.ColorOfHair = HairColor(4)
print('Peter\'s hair color',PeterParker.ColorOfHair)
print('Spiderman\'s hair color',SpiderMan.ColorOfHair)