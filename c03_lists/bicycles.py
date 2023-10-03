bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
for bicycle in bicycles:
    print(bicycle, end = ' ')

print()
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

#print last element
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)


#3-1 
names = ['elinna', 'caprice', 'vanya', 'iva', 'deska']
print(f"{names[0].title()}, {names[1].title()}, {names[2].title()}, {names[3].title()}, {names[4].title()} ")
for name in names:
    print(f"Hello, {name.title()} how are you today?")

cars = ['honda', 'suzuki', 'huyndai', 'bwm']
vehicles = ['car', 'truck', 'motorcycle']

print(f"I wold like to own a {cars[0].title()} {vehicles[0].title()}")


#change elements in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'bwm'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

new_moto_list = []
new_moto_list.append('first')
new_moto_list.append('second')
new_moto_list.append('third')
print(new_moto_list)

new_moto_list.insert(1, 'new_second')
print(new_moto_list)

del motorcycles[0]
print(motorcycles)

del new_moto_list[1]
print(new_moto_list)

popped_moto = motorcycles.pop()
print(motorcycles)
print(popped_moto)

popped_item = new_moto_list.pop(0)
print(new_moto_list)
print(popped_item)

#remove method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
