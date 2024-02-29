from vehiclePackage.CarClass import Car;  

class BMWX3(Car):
    def __init__(self, type, make, Max_speed):
        self.Max_speed = Max_speed;
        Car.__init__(self, type, make, Max_speed);
        
    def printMax_speed(self):
        print(self.Max_speed);