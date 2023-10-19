# Store information about a pizza bieng ordered.
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese']}
print(f"You ordered a {pizza['crust']}- crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
    
#favorite languages
favorite_languages = { 'jen': ['python', 'ruby'],
                       'sarah': ['c'],
                       'edward': ['ruby', 'go'],
                       'phil': ['python', 'haskell'] }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
