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
