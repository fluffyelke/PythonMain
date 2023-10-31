def make_pizza(*toppings):
    """
    Asterix to the arg name tells python to make an empty tuple
    Print the listo f toppings that have been requested.
    """
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 25, 56)

def modifyed_make_pizza(*toppings):
    """
    Summarie the pizza we are about to make.
    """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
modifyed_make_pizza('pepperoni')
modifyed_make_pizza('mushrooms', 'green peppers', 5, 15)
