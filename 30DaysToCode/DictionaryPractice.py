"""
Included here: Day 8 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""
#dictionaries in python are how one can use hash maps

#english to spanish dictionary
#key:value pairs in {} struct
EngEspDict = {'Monday':'Lunes',
'Tuesday':'Martes','Wednesday':'Miercoles',
'Thursday':'Jueves','Friday':'Viernes'}

#so we can see the evolution of the ESL to ESP dictionary
def PrintESLtoESP():
    print('Days of the week in English and Spanish (Key:Value pairs):')
    for key in EngEspDict:
        print(' ',key,'->',EngEspDict[key])

PrintESLtoESP()

def SizeOfESPtoESP():
    print('Number of {key:value} pairs in our English to Spanish dictionary:',\
        len(EngEspDict))

SizeOfESPtoESP()

#adding the weekend to the ESL to ESP dictionary we made
WeekEnd = {'Saturday':'Sabado','Sunday':'Domingo'}
for key in WeekEnd:
    if key in EngEspDict:
        continue
    else:
        EngEspDict[key] = WeekEnd[key]

#showing the additions
PrintESLtoESP()
SizeOfESPtoESP()

#new dict, shopping list
ShoppingList = {'Ham':True,'Bread':True,'Oreos':True,'Eggs':False,'Sugar':False}
for key in ShoppingList:
        print(' ',key,'->',ShoppingList[key])

print('Printing the entire dictioanry as it exists:\n',ShoppingList)
del ShoppingList['Eggs']
print('Printing the entire dictioanry as it exists after removing bread:\n',ShoppingList)
ShoppingList.pop('Sugar')
print('Printing the entire dictioanry as it exists after removing sugar:\n',ShoppingList)
