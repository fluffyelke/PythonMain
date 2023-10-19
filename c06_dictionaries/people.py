#6-7
#6-1
person_0 = {'first_name': 'vanya',
          'last_name': 'dimitrova',
          'age': 35,
          'city': 'sofia'}
person_1 = {'first_name': 'elinna',
          'last_name': 'georgieva',
          'age': 34,
          'city': 'sofia'}
person_2 = {'first_name': 'iva',
          'last_name': 'petrova',
          'age': 26,
          'city': 'sofia'}
person_list = [person_0, person_1, person_2]

for person in person_list:
    print(person)
    

#6-8
pet_0 = {
    'kind': 'cat',
    'owner': 'ivan'
    }
pet_1 = {
    'kind': 'dog',
    'owner': 'petrov'
    }
pet_2 = {
    'kind': 'owl',
    'owner': 'vanya'
    }
pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print(pet)
    
#6-9
favorite_places = {
    'vanya': ['sofia', 'plovdiv', 'karnobat'],
    'elinna': ['malaysia', 'sofia'],
    'iva': ['netherland', 'bulgaria']
    }
for name, places in favorite_places.items():
    print(f"{name.title()}, favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")
        
#6-2
persons_fav_numbers = {'vanya': [1, 5, 166],
                       'pesho': [10, 20],
                       'elinna': [1, 2, 3, 4, 5],
                       'deska': [5, 10, 15, 20, 25],
                       'gogo': [-1, -2, -3, -4, -5]}
for name, numbers in persons_fav_numbers.items():
    print(f"{name.title()} favorite numbers are:")
    for num in numbers:
        print(f"\t {num} ")
