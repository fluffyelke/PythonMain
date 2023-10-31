#9-1,  9-2,  9-3
class Restaurant:
    """
    Simple class representing restaurant.
    """
    def __init__(self, restaurant_name, cusine_type):
        """
        Constructor
        Initialize restaurant name and cusine cusine_type
        """
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0
#########################################
    
    def describe_restaurant(self):
        """
        Print information about the restaurant
        """
        print(f"Restaurant name: {self.restaurant_name.title()}.")
        print(f"Cusine type: {self.cusine_type.title()}.")
##########################################
    def open_restaurant(self):
        """
        Method to indicate that restaurant is open
        """
        print(f"{self.restaurant_name.title()} is open now!")
        
    def set_number_served(self, served):
        """
        Method to set the number of people served
        """
        self.number_served = served
        
    def increment_number_served(self, served, days):
        """
        Method do calculate how many people we served for a number of days
        """
        self.number_served = served
##############################################


dominos = Restaurant('dominos', 'pizza')
print(f"{dominos.restaurant_name.title()}, is serving {dominos.cusine_type.title()}.")
dominos.describe_restaurant()
dominos.open_restaurant()

vanyas_mechana = Restaurant('ivanovata mechana', 'traditional food')
kfc = Restaurant('KFC', 'checken food')
print(f"{vanyas_mechana.restaurant_name.title()}, is serving {vanyas_mechana.cusine_type.title()}.")
print(f"{kfc.restaurant_name.title()}, is serving {kfc.cusine_type.title()}.")

vanyas_mechana.describe_restaurant()
vanyas_mechana.open_restaurant()

kfc.describe_restaurant()
kfc.open_restaurant()

curr_restaurant = Restaurant('mcdonalds', 'burgers')
print(f"People servers {curr_restaurant.number_served}")
curr_restaurant.set_number_served(10)
print(f"People servers {curr_restaurant.number_served}")



#9-6
#Inheritance 
print("\n\n\nInheritance\n")
class IceCreamStand(Restaurant):
    """
    Represent a ice cream stand 
    """
    def __init__(self, restaurant_name, cusine_type):
        """
        Use super class constructor
        """
        super().__init__(restaurant_name, cusine_type)
        self.flavors = []
    #=====================================#
    def set_flavors(self, flavors_list = []):
        """
        Generate a list of ice cream flavors
        """
        self.flavors = flavors_list
        
    #=====================================#
    def print_flavors(self):
        """
        Method to print the ice cream flavors
        """
        for flavor in self.flavors:
            print(flavor)
    #======================================#
    
ice_cream_restaurant = IceCreamStand('raffy', 'ice cream')
ice_cream_restaurant.set_flavors(['pistachio', 'strawberry', 'choco', 'vanilla'])
ice_cream_restaurant.print_flavors()
