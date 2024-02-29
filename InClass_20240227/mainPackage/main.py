# main.py

# import the Vehicle class module
from vehiclePackage.vehicleClass import *

if __name__ == "__main__":
    # Instantiate an object of type Vehicle
    myCorvette = Vehicle("Car")
    myCorvette.printType()  # invoke the method 
    
    myCorolla = Vehicle("Toyota", 80)
    myCorolla.printType()
    print("Max Speed: ", myCorolla.getMaxSpeed())
    
    # Instantiate an object of type Hybrid
    