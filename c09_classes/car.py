class Car:
    """
    A simple attempt to represent a car.
    """
    def __init__(self, manifacturer, model, year):
        """
        Constructor
        Initialize attributes to describe a car.
        """
        self.manifacturer = manifacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
    #=======================================#
    
    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name.
        """
        long_name = f"{self.year} {self.manifacturer} {self.model}"
        return long_name.title()
    #=======================================#
    
    def read_odometer(self):
        """
        Print a statement showing the car's mileage.
        """
        print(f"This car has {self.odometer_reading} miles on it.")
    #=======================================#
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    #=======================================#
    
    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        """
        self.odometer_reading += miles
    #=======================================#
    
    
    #end of class Car
    
###############################################################


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(22)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print("\n\n\nInheritance\n")

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

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#9-9
print("\n\n9-9 exercise\n")
my_new_tesla = ElectricCar('tesla', 'model 3', 2021)
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.get_range()
my_new_tesla.battery.upgrade_battery()
my_new_tesla.battery.get_range()
