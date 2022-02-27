"""
Included here: Days 6 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

import random

class MadLibs():
    def __init__(self):
        self.Story = str()
        self.Name = str()
        self.Adjective1 = str()
        self.Adjective2 = str()
        self.Adjective3 = str()
        self.Noun1 = str()
        self.Noun2 = str()
        self.Noun3 = str()
        self.Adverb = str()
        self.RandomNums = int()

    #getters, just returning the property in question
    def GetStory(self):
        return self.Story 
    def GetName(self):
        return self.Name 
    def GetAdjective1(self):
        return self.Adjective1 
    def GetAdjective2(self):
        return self.Adjective2 
    def GetAdjective3(self):
        return self.Adjective3 
    def GetNoun1(self):
        return self.Noun1 
    def GetNoun2(self):
        return self.Noun2 
    def GetNoun3(self):
        return self.Noun3 
    def GetAdverb(self):
        return self.Adverb
    def GetRandomNums(self):
        return self.RandomNums

    #setters, no return needed, just an equal sign
    def SetStory(self,Story):
        self.Story = Story
    def SetName(self,Name):
        self.Name = Name
    def SetAdjective1(self,Adjective1):
        self.Adjective1 = Adjective1
    def SetAdjective2(self,Adjective2):
        self.Adjective2 = Adjective2
    def SetAdjective3(self,Adjective3):
        self.Adjective3 = Adjective3
    def SetNoun1(self,Noun1):
        self.Noun1 = Noun1
    def SetNoun2(self,Noun2):
        self.Noun2 = Noun2
    def SetNoun3(self,Noun3):
        self.Noun3 = Noun3
    def SetAdverb(self,Adverb):
        self.Adverb = Adverb
    def SetRandomNums(self):
        Num = random.randint(0,100)
        NumHolder = []
        for idx in range(0,3):
            NumHolder.append(Num + idx)
        self.RandomNums = "Not " + str(NumHolder[0]) + ", not "\
        + str(NumHolder[1]) + ", but " + str(NumHolder[2])

    #user inputs that call setters
    def EnterName(self):
        self.SetName(input('Please enter a name: '))
    def EnterAdjective1(self):
        self.SetAdjective1(input('Please enter an adjective: '))
    def EnterAdjective2(self):
        self.SetAdjective2(input('Please enter an adjective: '))
    def EnterAdjective3(self):
        self.SetAdjective3(input('Please enter an adjective: '))
    def EnterNoun1(self):
        self.SetNoun1(input('Please enter a noun: '))
    def EnterNoun2(self):
        self.SetNoun2(input('Please enter a noun: '))
    def EnterNoun3(self):
        self.SetNoun3(input('Please enter a noun: '))
    def EnterAdverb(self):
        self.SetAdverb(input('Please enter an adverb: '))

    def PrintInstructions():
        print('Welcome the MAD LIBS game! If you type in',\
        'words, we\'ll give you a story. Start by typing in a name.')

    def PutTogetherTheStory(self):
        RandoNum = random.randint(0,100) % 2
        if RandoNum == 0:
            Story = "Jesse and her best friend " + self.GetName() + " went to Disney World Today! " +\
            "They saw a " + self.GetNoun1() + " in a show at the Magic Kindom and ate a " +\
            self.GetAdjective1() + " feast for dinner. The next day I ran " + self.GetAdverb() +\
            " to meet Mickey Mouse in his " + self.GetNoun2() + " and then that night I gazed " +\
            " at the " + self.GetRandomNums() + " " + self.GetAdjective2() + " fireworks shooting from " +\
            " the " + self.GetNoun3() + "."
        else:
            Story = "Amanda and her frenemy " + self.GetName() + " went to the zoo last summer. " +\
            "They saw a huge " + self.GetNoun1() + " and a tiny little " + self.GetNoun3 +\
            " to get a closer look. The zoo was " + self.GetAdjective1 + " at night, but they didn't care... " +\
            "until " + self.GetRandomNums() + " " + self.GetAdjective2 + " apes yelled in their faces, making " +\
            "Amanda and " + self.GetName() + " run all the way home."
        self.SetStory(Story)

    def Play(self):
        MadLibs.PrintInstructions()
        self.EnterName()
        self.EnterNoun1()
        self.EnterNoun2()
        self.EnterNoun3()
        self.EnterAdjective1()
        self.EnterAdjective2()
        self.EnterAdjective3()
        self.EnterAdverb()
        self.SetRandomNums()
        self.PutTogetherTheStory()
        print(self.GetStory())

MyStory = MadLibs()
MyStory.Play()
