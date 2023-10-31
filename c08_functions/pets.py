def describe_pet(animal_type, pet_name):
    """
    Display information about a pet.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamester', 'micky')
describe_pet('dog', 'lilly')


# keyword arguments
def keyword_describe_pet(animal_type, pet_name):
    """
    Display information about a pet.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
keyword_describe_pet(animal_type = 'cat', pet_name = 'vanya')
keyword_describe_pet(pet_name = 'caprice', animal_type = 'dog')
