#8-3
def make_shirt(size, label):
    """
    Function to describe size and label of a t-shirt
    """
    print(f"Size: {size}, printet label {label.title()}.")

make_shirt(32, 'the north face')

make_shirt(size = 46, label = 'nike')

make_shirt(label = 'adidas', size = 25)

#8-4
def make_shift_defaults(size = 'large', label = 'I love Python'):
    """
    Function to check shirt size, label with defaults parameters
    """
    print(f"Size: {size}, label: {label}")
make_shift_defaults()
make_shift_defaults('medium')


#8-5
def describe_city(name, country = 'bulgaria'):
    """
    Print the city and the country where the city is.
    """
    print(f"{name.title()} is in {country.title()}");
    
describe_city('sofia', 'spain')
