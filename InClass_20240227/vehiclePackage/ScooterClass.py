from vehiclePackage.hybridClass import Hybrid; # This works but Eclipse flags an error in the editor.

class Scooter(Hybrid):
    def __init__(self, type_of_vehicle, make, model, batteryKVA):
        self.batteryKVA = batteryKVA;
        Hybrid.__init__(self, type_of_vehicle, make, model);
    def printBatteryKVA(self):
        print(self.batteryKVA);