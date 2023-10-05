cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
print(car == 'bmw', car == 'BMW', car.upper() == 'BMW')

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
    
age = 19
print(age < 21, age <= 21, age > 21, age >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print((age_0 >= 21) and (age_1 >= 21))


requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(('mushrooms' in requested_toppings), ('pepperoni' in requested_toppings))

