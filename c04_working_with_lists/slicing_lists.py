players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])     #get first 3 elements of the list

print(players[1:4])

print(players[:4])      #print from 0 to 3rd element included

print(players[2:])      #print from 3rd to the end

print(players[-3:])     #print last 3 elements

print("Looping through a slice")
print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())


numbers = list(range(1, 51))
print("First three elements are:")
print(numbers[:3])
print("Middle three elements are:")
print(numbers[23:26])
print("The Last three elements are:")
print(numbers[-3:])
