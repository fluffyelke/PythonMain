import json

"""
Load the username, if it has been stored previously.
Otherwise, promt for the username and store it.
"""

def get_stored_username():
    """
    Get stored username if available.
    """
    filename = 'username5.json'
    try:
        with open(filename) as my_file:
            username = json.load(my_file)
    except FileNotFoundError:
        return None
    else:
        return username
###############################
def get_new_username():
    """
    Prompt for a new username
    """
    username = input("What is your name? ")
    filename = 'username5.json'
    with open(filename, 'w') as my_file:
        json.dump(username, my_file)
    return username
#################################

def greet_user():
    """
    Greet user by name.
    """
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}! ")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}! ")
######################################################3
greet_user()

