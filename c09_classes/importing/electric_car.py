from car import Car

class Battery:
    """
    A simple attempt to model a battery for an electric car.
    """
    def __init__(self, battery_size = 75):
        """
        Initialize the battery's attributes.
        """
        self.battery_size = battery_size
    #===================================#
    def describe_battery(self):
        """
        Print a statement describing the battery size.
        """
        print(f"This car has a {self.battery_size}-kwh battery.")
    #===================================#
    def get_range(self):
        """
        Print a statement about the range this battery provides.
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")
        
    #===================================#
    #9-9
    def upgrade_battery(self):
        """
        Check battery size if is not 100 set it to 100
        """
        if self.battery_size != 100:
            self.battery_size = 100
    #===================================#
    
    #end class Battery
########################################
class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles.
    """
    def __init__(self, manifacturer, model, year):
        """
        Initialize attributes of the parent class.
        """
        super().__init__(manifacturer, model, year)
        
        #electric car members
        self.battery = Battery()        #create a instance of a class Battery()
    #=============================================#
    
    def describe_battery(self):
        """
        Print a statement describing the battery size.
        """
        print(f"This car has a {self.battery_size}-kwh battery.")
    #=============================================#
    
    
################################################################
#End of class ElectricCar
