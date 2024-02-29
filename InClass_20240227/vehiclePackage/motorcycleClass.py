from vehiclePackage.vehicleClass import *

class motorcycle(Vehicle):  # Car inherits from Vehicle
    def __init__(self, type_of_vehicle, make, model, year):
        self.make = make;
        self.model = model;
        Vehicle.__init__(self, type_of_vehicle);
        self.year = year;
        
    def printMake(self):
        print(self.make);
    
    def printModel(self):
        print(self.model);
        
    def printYear(self):
        print(self.year)
