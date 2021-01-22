class Pet:
    def __init__(self,name,age,hunger,playful):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.playful = playful

    #getters
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getHunger(self):
        return self.hunger
    
    def getPlayful(self):
        return self.playful

    #setters

    def setName(self,set_name):
        self.name = set_name
    
    def setAge(self,set_age):
        self.age = set_age
    
    def setHunger(self,set_hunger):
        self.hunger = set_hunger

    def setPlayful(self,set_playful):
        self.playful = set_playful

class Dog(Pet):
    def __init__(self,name,age,hunger,playful,breed,favoriteToy):
        Pet.__init__(self,name,age,hunger,playful)
        self.breed = breed
        self.favoriteToy = favoriteToy

    def wantsToPlay(self):
        if self.playful  == True:
            return("Dog wants to play with "+self.favoriteToy)
        else:
            return ("Dog doesn't want to play")

class Cat(Pet):
    def __init__(self,name,age,hunger,playful,favoritePlaceToSit):
        Pet.__init__(self,name,age,hunger,playful)
        self.favoritePlaceToSit = favoritePlaceToSit

    def wantsToSit(self):
        if self.playful == False:
            print("The Cat wants to site in",self.favoritePlaceToSit)
        else:
            print("The Cat wants to play")

class Human:
    def __init__(self,name,pets):
        self.name = name
        self.pets = pets

    def hasPets(self):
        if len(self.pets) != 0:
            return "yes"
        else:
            return "no"

huskyDog = Dog("Flame",3,True,True,"Siverian","Bone")

Play = huskyDog.wantsToPlay()

print(Play)

typicalCat = Cat("Fluffy",3,True,False,"Chair")

typicalCat.wantsToSit()

yourAverageHuman = Human("Alex",[huskyDog,typicalCat])

hasPet = yourAverageHuman.hasPets()

print(hasPet)
