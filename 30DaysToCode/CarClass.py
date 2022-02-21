"""
Included here: Days 1,2,3,4 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

class Car: #this is how we declare and define classes in python
    def __init__(self,MaxSpeed = 100, MinSpeed = 0, Weight = 100, IsTheCarOn = False, Condition = 'A', NameOfCar = 'Lucy',\
        MaxFuel = 16, CurrentFuel = 8, mpg = 24.6, NumPeopleInTheCar = 1, MaxPeopleInCar = 5): 
        # this is a default contructor function if it only takes in self, it will create an object with its defined 
        # properties below, and only accept one argument which is the reference to the instance of the class that is 
        # being contructed (self). Its called a parameterized contructor if it takes in parameters.
        
        #these are properties, represented by different data types and will be used to define things about objects of class car.
        self.MaxSpeed = MaxSpeed #mph
        self.MinSpeed = MinSpeed #mph
        self.Weight = Weight #weight in pounds
        self.IsTheCarOn = IsTheCarOn
        self.Condition = Condition
        self.NameOfCar = NameOfCar
        self.MaxFuel = MaxFuel #Gallons
        self.CurrentFuel = CurrentFuel #Gallons
        self.mpg = mpg
        self.NumPeopleInCar = NumPeopleInTheCar #Has to be an integer to make any kind of sense
        self.MaxPeopleInCar = MaxPeopleInCar #Has to be an integer to make any kind of sense

        #getters 
        def getMaxSpeed(self):
            return self.MaxSpeed
        def getMinSpeed(self):
            return self.MinSpeed
        def getWeight(self):
            return self.Weight
        def getIsTheCarOn(self):
            return self.IsTheCarOn
        def getCondition(self):
            return self.Condition
        def getNameOfCar(self):
            return self.NameOfCar
        def getMaxFuel(self):
            return self.MaxFuel
        def getCurrentFuel(self):
            return self.CurrentFuel
        def getmpg(self):
            return self.mpg
        def getNumPeopleInCar(self):
            return self.NumPeopleInCar
        def getMaxPeopleInCar(self):
            return self.MaxPeopleInCar

        #setters 
        def setMaxSpeed(self,MaxSpeed):
            self.MaxSpeed = MaxSpeed
        def setMinSpeed(self,MinSpeed):
            self.MinSpeed = MinSpeed
        def setWeight(self,Weight):
            self.Weight = Weight
        def setIsTheCarOn(self,IsTheCarOn):
            self.IsTheCarOn = IsTheCarOn
        def setCondition(self,Condition):
            self.Condition = Condition
        def setNameOfCar(self,NameOfCar):
            self.NameOfCar = NameOfCar
        def setMaxFuel(self,MaxFuel):
            self.MaxFuel = MaxFuel
        def setCurrentFuel(self,CurrentFuel):
            self.CurrentFuel = CurrentFuel
        def setmpg(self,mpg):
            self.mpg = mpg
        def setNumPeopleInCar(self,NumPeopleInCar):
            self.NumPeopleInCar = NumPeopleInCar
        def setMaxPeopleInCar(self,MaxPeopleInCar):
            self.MaxPeopleInCar = MaxPeopleInCar

        #this is an instance method, it accesses and shows the definitions of properties of a specific instance of the class.
        #this method can only be used if an instance of the car class is created to be used on.
    def PrintVariables(self):
        print('----START OF PRINT VARIABLES----')
        print('Max Speed:         ', self.MaxSpeed,'MPH')
        print('Min Speed:         ', self.MinSpeed,'MPH')
        print('Weight:            ', self.Weight,'LBS')
        print('Is Car On:         ', self.IsTheCarOn)
        print('Condition:         ', self.Condition)
        print('Name of Car:       ', self.NameOfCar)
        print('Num People in Car: ', self.NumPeopleInCar,'People')
        print('-----END OF PRINT VARIABLES-----')
    
    def WreckCar(self):
        self.Condition = 'C'

    def UpgradeMinSpeed(self):
        self.MinSpeed = self.MaxSpeed
        self.MaxSpeed += 100
    
    def GetIn(self,NumOfPeople):
        if self.NumPeopleInCar + NumOfPeople <= self.MaxPeopleInCar:
            self.NumPeopleInCar += NumOfPeople
            print('The new number of people in the car is: ',self.NumPeopleInCar)
        else:
            print('That\'s too many people trying to get in the car, there\'s not enough space!')

    def GetOut(self,NumOfPeople):
        if self.NumPeopleInCar > 0 and self.NumPeopleInCar - NumOfPeople >= 0:
            self.NumPeopleInCar -= NumOfPeople
            print('The new number of people in the car is: ',self.NumPeopleInCar)
        else:
            print('That\'s more people that are actually in the car!')

    def HowManyMilesToEmpty(self):
        print('Miles to Empty: ', self.CurrentFuel * self.mpg,'MILES')

    def RangeWithFullTank(self):
        print('Range With Full Tank: ', self.MaxFuel * self.mpg,'MILES')

    def TurnCarOn(self):
        if self.IsTheCarOn == False:
            self.IsTheCarOn = True
            print('The car has been turned on.')
        else:
            print('The car is already on.')

    


#Declaration, Assignment, And Instantiation of a class of type Car called FredsCamry, invoking and instance method
FredsCamry = Car()
FredsCamry.PrintVariables()

#FredsCamry is a reference type and Dalais camry is pointing to the same place in memory so changing one, changes both
DaliasCamry = FredsCamry
DaliasCamry.MaxSpeed = 120
FredsCamry.PrintVariables()
DaliasCamry.WreckCar()
FredsCamry.PrintVariables()
FredsCamry.UpgradeMinSpeed()
FredsCamry.PrintVariables()
FredsCamry.GetIn(2)
FredsCamry.PrintVariables()
FredsCamry.HowManyMilesToEmpty()
FredsCamry.RangeWithFullTank()
FredsCamry.TurnCarOn()
FredsCamry.TurnCarOn()
FredsCamry.TurnCarOn()
FredsCamry.GetOut(2)
FredsCamry.GetOut(100)
FredsCamry.GetIn(3)
FredsCamry.GetIn(100)