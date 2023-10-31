class User:
    """
    Class to represent a simple user.
    """
    def __init__(self, first_name, last_name):
        """
        Constructor
        Takes 2 arguments and initialize them.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    #===========================================#
    def describe_user(self):
        """
        Method to print the user information.
        """
        print(f"{self.first_name.title()} {self.last_name.title()}")
    #=======================================#
    def greet_user(self):
        """
        Method to simple greet the user.
        """
        print("Greetings",end = ' ')
        self.describe_user()
    #=======================================#
    def increment_loggin_attempts(self):
        """
        Method that increment login attempts by 1
        """
        self.login_attempts += 1
    #=======================================#
    def reset_login_attempts(self):
        """
        Method that reset login attempts to 0
        """
        self.login_attempts = 0
    #=======================================#    
    def print_login_attempts(self):
        """
        Print current number of login attempts
        """
        print(self.login_attempts)
#################################################

vanya = User('vanya', 'dimitrova')
vanya.greet_user()
vanya.describe_user()

elinna = User('elinna', 'georgieva')
elinna.greet_user()
elinna.increment_loggin_attempts()
elinna.increment_loggin_attempts()
elinna.increment_loggin_attempts()
elinna.describe_user()
print(f" has logged ", end = ' ')
elinna.print_login_attempts()


#9-7
print("\n\n\nInheritance\n")

#9-8
class Privileges:
    """
    Class representing the admin privileges.
    """
    def __init__(self, privileges = []):
        """
        Constructor, set user admin privileges in a list
        """
        self.privileges = privileges
    #====================================#
    def show_privileges(self):
        """
        Show user admin privileges
        """
        print(self.privileges)
    #====================================#
    
class Admin(User):
    """
    Class representing IT admin.
    """
    def __init__(self, first_name, last_name):
        """
        Constructor add super class functionallity
        """
        super().__init__(first_name, last_name)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user2'])
    #===========================================#
    
    def show(self):
        """
        Method to print the admin privileges.
        """
        self.privileges.show_privileges()
    #===========================================#


vanya_admin = Admin('vanya', 'dimitrova')
vanya_admin.show()
