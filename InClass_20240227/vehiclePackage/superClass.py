from vehiclePackage.CarClass import Car; # This works but Eclipse flags an error in the editor.

class Super(Car):
    def __init__(self, type_of_vehicle, make, model, batteryKVA):
        self.batteryKVA = batteryKVA;
        Car.__init__(self, type_of_vehicle, make, model);
    def printBatteryKVA(self):
        print(self.batteryKVA);