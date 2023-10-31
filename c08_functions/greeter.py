def greet_user():
    """
    Display a simple greeting.
    """
    print("Hello")

greet_user()


def greet_user(username):
    """
    Display a simple greeting to the username.
    """
    print(f"Hello {username.title()}.")

greet_user('vanya')


def display_message():
    """
    Print a simple message
    """
    print("This is my function call.")
display_message()

def favorite_book(book_title):
    """
    Function that print favorite title
    """
    print(f"My favorite book is: {book_title.title()}")
favorite_book('Rozhdenichkata')


def get_formatted_name(first_name, last_name):
    """
    Return a full name, neatly formatted.
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#this is infinite loop
while True:
    
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
