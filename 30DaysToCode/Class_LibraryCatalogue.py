"""
Library Catalogue Class
Included here: Day 11 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""
#for this to work Class_book needs to be in the same directory as this script
#import Class_Book as CB
import Class_Book as cb 

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
    def CheckOut(self,BookTitle):
        Book = self.BookCollection[BookTitle]
        if Book.GetIsCheckedOut() == True:
            self.BookAlreadyCheckedOut(Book)
        else:
            Book.SetIsCheckedOut(True,self.CurrentDay)
            print(f'You just checked out {BookTitle}.',\
                f'It is due on {self.GetCurrentDay() + self.GetLengthOfCheckoutPeriod()}.')


    def ReturnBook(self,BookTitle):
        Book = self.BookCollection[BookTitle]
        DaysLate = self.CurrentDay - (Book.GetDayCheckedOut() + self.GetLengthOfCheckoutPeriod())
        if DaysLate > 0:
            print(f'You owe the library {self.GetInitialLateFee() + DaysLate*self.GetFeePerLateDay()}',\
                f'because your books is {DaysLate} days overdue.')
        else:
            print('Books is returned, thank you.')
        Book.SetIsCheckedOut(False,-1)

    def BookAlreadyCheckedOut(self,Book):
        print(f'Sorry {Book.GetTitle()} is already checked out.',\
            f'It should be back on day {Book.GetDayCheckedOut()+self.GetLengthOfCheckoutPeriod()}.')

TestBook1 = cb.Book('Life of Freddy',420,696969,False,1)
TestBook2 = cb.Book('Life of Dalia',69,420420,True,2)

#Testing my methods, I'm a librarian!
TestLib = LibraryCatalogue(CurrentDay = 10,LengthOfCheckoutPeriod=6,BookCollection={TestBook1.Title:TestBook1,TestBook2.Title:TestBook2})
TestLib.CheckOut(TestBook1.Title)
TestLib.CheckOut(TestBook2.Title)
TestLib.ReturnBook(TestBook2.Title)
TestLib.ReturnBook(TestBook1.Title)
print(TestLib.BookCollection)