"""
Included here: Day 11 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""
#for this to work Class_book needs to be in the same directory as this script
#import Class_Book as CB


class LibraryCatalogue:

    #contructor
    def __init__(self,CurrentDay = 0,LengthOfCheckoutPeriod = 7,InitialLateFee = .5,FeePerLateDay = 1,\
        BookCollection = {}):

        #properties
        self.CurrentDay = CurrentDay
        self.LengthOfCheckoutPeriod = LengthOfCheckoutPeriod
        self.InitialLateFee = InitialLateFee
        self.FeePerLateDay = FeePerLateDay
        self.BookCollection = BookCollection

    #getters
    def GetCurrentDay(self):
        return self.CurrentDay
    def GetLengthOfCheckoutPeriod(self):
        return self.LengthOfCheckoutPeriod
    def GetInitialLateFee(self):
        return self.InitialLateFee
    def GetFeePerLateDay(self):
        return self.FeePerLateDay
    def GetBookCollection(self):
        return self.BookCollection
    def GetBook(self,BookTitle):
        self.GetBookCollection()[BookTitle]

    #setters
    def NextDay(self):
        self.CurrentDay += 1
    def SetCurrentDay(self,CurrentDay):
        self.CurrentDay = CurrentDay

    #instance methods
    def CheckOut(BookTitle):

    def ReturnBook(BookTitle):
    
    def BookAlreadyCheckedOut(BookTitle):

        

    