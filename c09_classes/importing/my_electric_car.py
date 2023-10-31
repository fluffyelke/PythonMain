#import multiple classes
from car import Car
from electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

#import entire module
import car

my_audi = car.Car('audi', 'a4', 2019)
my_electric_audi = ElectricCar('audi', 'e-tron', 2022)

print(my_audi.get_descriptive_name())
print(my_electric_audi.get_descriptive_name())


#import all classes from a module
#from car import *
