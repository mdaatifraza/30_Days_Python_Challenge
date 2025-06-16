# Inheritance

class vehicle:
    def general_usage(self):
        print("General use : Transportation" )

class car(vehicle):  # Inheritance of class
    def __init__(self):
        print(f'I am a car')
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print(f'Specific use : commute to work, vacation with family.')

class MotorCycle(vehicle):
    def __init__(self):
        print(f'I am a Motor Cycle')
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print(f'Specific use is : road trip and racing')


class electric_car(car):
    def __init__(self, make, model, battery):
        self.make = make
        self.model = model
        self.battery = battery

    def display(self):
        print(f'The {self.make} {self.model} is an electric car with a battery capacity of {self.battery} kWh')


c = car()
c.general_usage()     # we can call the main class
c.specific_usage()
print("--------------------------------------------------------------")

e_c = electric_car("Tesla", "Model 3", 75)
e_c.display()
e_c = electric_car("Nissan", "Leaf", 40 )
e_c.display()
e_c = electric_car("Hyundai", "Ioniq 5", 40.5 )
e_c.display()

print("------------------------------------------------------")
M = MotorCycle()
M.general_usage()
M.specific_usage()

#-----------------🎯 Challenge-----------------
#------------------ Extend Car into an ElectricCar subclass with battery capacity-----------------

