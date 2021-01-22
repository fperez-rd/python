"""
programmer: Felix Perez

Homeworks #9: Classes

Details:
 
Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".

The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.

Next an inheritance classes from Vehicle called "Cars".

The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.  It should have another method 
called "Stop" that sets the value of isDriving to false.

Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter. And when TripsSinceMaintenance 
exceeds 100, then the NeedsMaintenance boolean should be set to true.

Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.

Create 3 different cars, using your Cars class, and drive them all a different number of times. Then print out their values for 
Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance

Extra Credit:

Create a Planes class that is also an inheritance class from Vehicle. Add methods to the Planes class for Flying and 
Landing (similar to Driving and Stopping), but different in one respect: Once the NeedsMaintenance boolean gets set to true, any 
attempt at flight should be rejected (return false), and an error message should be printed saying that the plane can't fly until it's repaired.
"""

class Vehicle:
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance

    def set_Make(self,Make):
        self.Make = Make

    def set_Model(self,Model):
        self.Model = Model

    def set_Year(self,Year):
        self.Year = Year
    
    def set_Weight(self,Weight):
        self.Weight = Weight

    def set_NeedsMaintenance(self,NeedsMaintenance):
        self.NeedsMaintenance = NeedsMaintenance

    def set_TripsSinceMaintenance(self,TripsSinceMaintenance):
        self.TripsSinceMaintenance = TripsSinceMaintenance

    def set_Weight(self,Weight):
        self.Weight = Weight

    def get_Make(self):
        return self.Make

    def get_Model(self):
        return self.Model
    
    def get_Year(self):
        return self.Year

    def get_Weight(self):
        return self.Weight

    def set_NeedsMaintenance(self):
        return self.NeedsMaintenance

    def set_TripsSinceMaintenance(self):
        return self.TripsSinceMaintenance

class Cars(Vehicle):
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0,isDriving=False):
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
        self.isDriving = isDriving

    def Drive(self):
        if self.isDriving == False:    
            self.isDriving = True

    def Stop(self):

        if self.isDriving == True:
            self.TripsSinceMaintenance = self.TripsSinceMaintenance + 30

        if self.TripsSinceMaintenance  > 100:
            self.NeedsMaintenance = True
            self.TripsSinceMaintenance = 0

        self.isDriving = False

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    def __str__(self):
        output = "Make: "+str(self.Make)+", Model: "+self.Model+", Year: "+str(self.Year)+", Weight: "+str(self.Weight)+", Needs Maintenance: "+str(self.NeedsMaintenance)+", Trips Since Maintenance: "+str(self.TripsSinceMaintenance)
        return output

class Planes(Vehicle):
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0,isFlying=False):
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)

    def Fliying(self):
        if self.isFlying == False:
            if self.NeedsMaintenance == True:
                print("the plane can't fly until it's repaired")    
            else:
                self.isFlying = True

    def Landing(self):

        if self.isFlying == True:
            self.TripsSinceMaintenance = self.TripsSinceMaintenance + 30

        if self.TripsSinceMaintenance  > 100:
            self.NeedsMaintenance = True
            self.TripsSinceMaintenance = 0

        self.isFlying = False

ferrary488 = Cars(2015,"488",2015,3252)
porsche918Spider = Cars(2013,"918 Spyder",2013,3792)
bugattiVeyron = Cars(2011,"Veyron 16.4",2015,4052)

ferrary488.Drive()
ferrary488.Stop()
ferrary488.Drive()
ferrary488.Stop()
ferrary488.Drive()

print(ferrary488)

porsche918Spider.Drive()
porsche918Spider.Stop()
porsche918Spider.Drive()
porsche918Spider.Stop()
porsche918Spider.Drive()
porsche918Spider.Stop()
porsche918Spider.Drive()
porsche918Spider.Stop()
porsche918Spider.Drive()
porsche918Spider.Stop()
porsche918Spider.Drive()
porsche918Spider.Stop()

print(porsche918Spider)


bugattiVeyron.Drive()
bugattiVeyron.Stop()
bugattiVeyron.Drive()
bugattiVeyron.Stop()
bugattiVeyron.Drive()
bugattiVeyron.Stop()

print(bugattiVeyron)