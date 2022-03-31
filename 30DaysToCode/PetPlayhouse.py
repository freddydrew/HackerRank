"""
Pet Playhouse - Testing the Animal, Dog, and Cat Classes
Included here: Day 12, 13 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""
# import Class_Dog as d
# doggy = d.Dog(7) 

##Anything from these files will be created if i leave an instance in the othert files?
# from Class_Animal import Animal
from re import L
from Class_Dog import Dog
from Class_Cat import Cat
from Class_Animal import Animal
# A = Animal(5) #Cant do this, its an abstract class
D = Dog(10) #instantiate a dog 
D.Ruff() #instance method
C = Cat() #instantiate a cat
C.Meow() #instance method
# A.Eat() #Cant do this, its an abstract class
D.Eat() #overrides the abstract method in animal class
C.Eat() #overrides the abstract method in animal class
D.Run() #instance method 
C.Prance() #instance method
print(D.GetAge()) #overrides the abstract method in animal class
print(C.GetAge()) #overrides the abstract method in animal class
D.Sleep()  #overrides the class method in animal class
C.Sleep() #doesn't overide the class method, therefore it uses the class method
print(dir(D))

#In java, you cant say Dog D = New Animal[], because dog is an animal. You could do it the other way
#but you'd be limited to only the animal methods, not the dog.

if isinstance(D,Animal):
    print('Dog is an Animal')
    Animal.Sleep()