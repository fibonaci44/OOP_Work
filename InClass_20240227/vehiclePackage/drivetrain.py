from vehiclePackage.hybridClass import Hybrid; # This works but Eclipse flags an error in the editor.

class drivetrainConfiguration(Hybrid):
    def __init__(self, type, make, model, drivetrain):
        self.drivetrain = drivetrain;
        Hybrid.__init__(self, type, make, model);
    def printBatteryKVA(self):
        print(self.drivetrain);