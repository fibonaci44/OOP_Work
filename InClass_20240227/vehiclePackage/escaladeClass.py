#escaladeClass.py
# Name: Brianna Jarrell
# email: jarrelbc@mail.uc.edu
# Assignment Number: InClass_20240227
# Due Date: 
# Course/Section: IS 4010 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Introduction to OOP
# Citations:
# Anything else that's relevant:

from vehiclePackage.vehicleClass import *;
class Escalade(Vehicle): # Car inherits from vehicle (Vehicle is the base class of Car)
    def __init__(self, type_of_vehicle, make, model):
        self.make = make;
        self.model = model;
        Vehicle.__init__(self, type_of_vehicle);
        
    def printMake(self):
        print(self.make);
        
    def printModel(self):
        print(self.model);
        