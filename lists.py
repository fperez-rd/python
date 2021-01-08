"""

programmer: Felix Perez
Homework Assignment #4: Lists

*This program use a function to add elements to a list and evaluate through functions of non-uniqueness.

"""

#Global variable list

myUniqueList = []
myLeftovers = []

#functions

def rejectedList(Input):
    myLeftovers.append(Input)
def modifyList(Input):

    Output = False

    if Input in myUniqueList:
        Output = False
        rejectedList(Input)
    else:
        myUniqueList.append(Input)
        Output = True

    return Output

#test funtion

modifyList("Hello")
modifyList("Word")
modifyList("Hello")
modifyList("Python is the best language programming")
modifyList(1)
modifyList(2)
modifyList(3)
modifyList(4)
modifyList("Python is the best")
modifyList(2)
modifyList(1)
modifyList(2)
modifyList("Python is the best language programming")
modifyList("Hello")

#print result in CLI
print(myUniqueList)
print(myLeftovers)