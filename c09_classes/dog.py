class Dog:
    """
    A simple attempt to model a dog.
    """
    #Constructors
    def __init__(self, name, age):
        """
        Constructor
        Initialize name and age attributes.
        """
        self.name = name
        self.age = age
        
    #Methods
    def sit(self):
        """
        Simulate a dog sitting in response to a command.
        """
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """
        simulate rolling over in response to a command.
        """
        print(f"{self.name} rolled over!")
        
#end of class Dog


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

vanya_dog = Dog('Vanya', 12)
print(f"\nYour dog's name is {vanya_dog.name}.")
print(f"Your dog is {vanya_dog.age} years old.")
vanya_dog.sit()
vanya_dog.roll_over()
