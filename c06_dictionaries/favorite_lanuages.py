favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#if the key doesnt exist, we can use get() method and on second argument to pass the throw information
alien_0 = {'color': 'green', 
           'speed': 'slow'}

point_value = alien_0.get('points', 'No Point value assigned.')
print(point_value)

#alternative approach
key_value = 'points'
point_value = alien_0.get(key_value, f"'{key_value}', was not found in the dictionary")
print(point_value)

#6-1
person = {'first_name': 'vanya',
          'last_name': 'dimitrova',
          'age': 35,
          'city': 'sofia'}
print(person)
for elem in person:
    print(elem, ' -> ', person[elem])
    
#6-2
persons_fav_numbers = {'vanya': 1,
                       'pesho': 2,
                       'elinna': 3,
                       'deska': 4,
                       'gogo': 5}
print(persons_fav_numbers)

#6-3
key_words = {'for': 'cycle through the elements from...to',
             'while': 'same as "for" cycle',
             'list': 'an container to hold items',
             'dictionary': 'key...value container',
             'if': 'conditional statement',
             'do_while': 'same as while but always run atleast once',
             'operators': '-,+,*,/ arithmethic operators',
             'something': 'nothing',
             'word': 'aham',
             'number': 5}
for elem in key_words:
    print(elem, '\n\t', key_words[elem] )
    
