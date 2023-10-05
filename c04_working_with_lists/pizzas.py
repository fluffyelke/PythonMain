#4-1
pizzas = ['margarita', 'fungi', 'ham']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("I really like pizza")

#4-2
animals = ['cat', 'lion', 'tiger']
for animal in animals:
    print(f"A {animal.title()} would make a great pet")
print("And this is all about small and big cats")


#4-11
friend_pizzas = pizzas[:]
print("MyPizzas:")
print(pizzas)
print("Friend Pizzas:")
print(friend_pizzas)
pizzas.append('pepperoni')
friend_pizzas.append('cheese')
print("After MyPizzas:")
print(pizzas)
print("After Friend Pizzas:")
print(friend_pizzas)

for pizza in pizzas:
    print(f"My favorite pizzas are {pizza.title()}")
    
print()
for pizza in friend_pizzas:
    print(f"My Friends favorite pizzas are {pizza.title()}")
