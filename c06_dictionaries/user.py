user_0 = {'username': 'efermi', 
          'first': 'enrico',
          'last': 'fermi'}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favotite language is: {language.title()}.")
    
#looping through all the keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())
    
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")
        
if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')
    
#sorted
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
#using values instead of keys
print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())
    
    
#printing unique values using set method
print('The following unique languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
