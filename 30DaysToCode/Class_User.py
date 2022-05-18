"""
User Class
Included here: Day 28 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

class User():

    def __init__(self,username,password,age,orderID) -> None:
        self.username = username
        self.password = password
        self.age = age
        self.orderID = orderID


mySet = set()
mySet.add(1212)

Freddy = User('freddydrew','codeboi',27,mySet)


