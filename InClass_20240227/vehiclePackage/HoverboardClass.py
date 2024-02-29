from vehiclePackage.vehicleClass import *;

class Hoverboard(Vehicle):  # Car inherits from Vehicle
    def __init__(self, type_of_board, make, model):
        self.make = make;
        self.model = model;
        Hoverboard.__init__(self, type_of_board);
        
    def printMake(self):
        print(self.make);
    
    def printModel(self):
        print(self.model);