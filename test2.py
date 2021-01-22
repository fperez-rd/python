class Dog:
  def __init__(self,name="Jack"):
    self.name = name

  def getName(self):
    return self.name

  def setName(self,Name):
    self.name = Name

myDog = Dog("Rolfie")
firstName = myDog.name
myDog.setName("Bobby")
secondName = myDog.getName()