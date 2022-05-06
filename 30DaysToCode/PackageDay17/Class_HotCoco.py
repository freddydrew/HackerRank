"""
Hot Coco
Included here: Day 17 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

from PackageDay17.Class_TempException import TempException

class HotCoco(TempException):
    def __init__(self,temp):
        super().__init__(temp)
        print('We\'ve got some hot coco here.')
        self.TooHot = self.TooHotException()
        self.TooCold = self.TooColdException()


    def TooHotException(self):
        if self.temp >= 185:
            raise Exception('THIS SHIT IT HOT BRO!')
        return "No exception"

    def TooColdException(self):
        if self.temp <= 165:
            raise Exception('This is too cold bro.')
        return "No exception"


