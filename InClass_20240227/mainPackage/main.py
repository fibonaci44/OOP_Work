# main.py

# import the Vehicle class module
from vehiclePackage.vehicleClass import *
from vehiclePackage.hybridClass import Hybrid

from vehiclePackage.fastCarClass import *
from vehiclePackage.engineClass import Engine

if __name__ == "__main__":
    # Instantiate an object of type Vehicle
    myCorvette = Vehicle("Car")
    myCorvette.printType()  # invoke the method 
    
    myCorolla = Vehicle("Toyota", 80)
    myCorolla.printType()
    print("Max Speed: ", myCorolla.getMaxSpeed())
    
    # Instantiate an object of type Hybrid
    myPrius = Hybrid("Car", "Toyota", "Prius", 222)
    print(myPrius.printModel())
    
    #a really fast car
    myFastPrius = fastCar("Car", "Cruz", 100000)
    print(myFastPrius.printModel())
    myCar = Engine("Sports", 5.0)
    print(myCar.printModel())
