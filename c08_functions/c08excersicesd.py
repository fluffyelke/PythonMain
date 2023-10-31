#8-12
def make_sandwich(*items):
    """
    Get a list from the user
    """
    for item in items:
        print(item, end = ' ')
    print()
make_sandwich('one', 'two', 'three')
make_sandwich(1, 2, 3, 5, 6)
make_sandwich('vanya', 'elinna', 'caprice', 5, 10, 'alaina')


#8-13
def build_person(first, last, **person):
    """
    Build a person with first and last name, and skills that the person has
    """
    person['first'] = first
    person['last'] = last
    return person

print(build_person('vanya', 'dimitrova', 
                   work = 'archtect',
                   age = 35,
                   location = 'sofia'))
list_of_persons = [build_person('alaina', 'dawson',
                                work = 'programmer',
                                age = 25), 
                   build_person('elinna', 'georgieva',
                                work = 'veolia',
                                age = 35)]
print(list_of_persons)

#8-14
def car_infoarmation(brand, model, **kwargs):
    """
    Get information for a car
    """
    kwargs['brand'] = brand
    kwargs['model'] = model
    return kwargs

car = car_infoarmation('subaru', 'outback', color = 'blue', tow_package = True)
print(car)
