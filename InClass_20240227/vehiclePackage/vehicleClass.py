# vehicleClass.py

'''
Vehicle Class
This class models a vehicle for sale on a car lot
Corresponding design document #
Author: 
Change order: We need max speed as part of our class
Change order: We need a way to get the max speed out of the object
  Translation: write a method that returns the max speed
Change Order: Add a getType method
  
'''

class Vehicle:
    # Constructor. Invoked whenever an object of this type is instantiated
    def __init__(self, type, maxSpeed = -1):
        self.type = type;
        self.maxSpeed = maxSpeed; # store max speed in a instance-level variable
 
    def printType(self):
        print(self.type);

    def getMaxSpeed(self):
        '''
        @return: maximum speed of the Vehicle
        '''
        return self.maxSpeed
    
    def getType(self):
        '''
        @return: Vehicle type
        '''
        return self.type
    
if __name__ == "__main__":
    # Some code to test the class would go here.
    # If there's no code, just pass
    pass
