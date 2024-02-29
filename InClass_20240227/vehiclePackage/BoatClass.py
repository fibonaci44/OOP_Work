from vehiclePackage.vehicleClass import *;           

class Boat(Vehicle):
    def __init__(self, type_of_vehicle, make, model):
        self.make = make;
        self.model = model;
        Vehicle.__init__(self, type_of_vehicle);
