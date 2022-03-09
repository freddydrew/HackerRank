"""
Book Class
Included here: Day 11 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

class Book:

    def __init__(self, Title = None, PageCount = 0, ISBN = 0, IsCheckedOut = False, DayCheckedOut = 0):
        self.Title = Title
        self.PageCount = PageCount
        self.ISBN = ISBN
        self.IsCheckedOut = IsCheckedOut
        self.DayCheckedOut = DayCheckedOut

    #getters
    def GetTitle(self):
        return self.Title
    def GetPageCount(self):
        return self.PageCount
    def GetISBN(self):
        return self.ISBN
    def GetIsCheckedOut(self):
        return self.IsCheckedOut
    def GetDayCheckedOut(self):
        return self.DayCheckedOut
    
    #setters, __ before method names denotes that they are private
    def SetTitle(self,Title):
        self.Title = Title  
    def SetPageCount(self,PageCount):
        self.PageCount = PageCount
    def SetISBN(self,ISBN):
        self.ISBN = ISBN
    def SetIsCheckedOut(self,IsCheckedOut,CurrentDay):
        self.IsCheckedOut = IsCheckedOut
        self.__SetDayCheckedOut(CurrentDay) #this method can only be accessed in the class
    def __SetDayCheckedOut(self,DayCheckedOut): #cannot be used outside of the class
        self.DayCheckedOut = DayCheckedOut
    
