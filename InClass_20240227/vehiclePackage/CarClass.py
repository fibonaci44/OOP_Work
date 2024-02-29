from vehiclePackage.vehicleClass import *;

class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, type_of_vehicle, make, model):
        self.make = make;
        self.model = model;
        Vehicle.__init__(self, type_of_vehicle);
        
    def printMake(self):
        print(self.make);
    
    def printModel(self):
        print(self.model);
