alien_0 = {'color': 'green',
           'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print(alien_0)
#add new elements to the dictionoary
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25

print(alien_0)

#modify a value in a dictionoary
print("Old dictionary")
print(alien_0)

alien_0['color'] = 'yellow'
print(f"The new dictionary contains now:")
print(alien_0)


alien_0 = {'x_pos': 0, 
           'y_pos': 25,
           'speed': 'medium'}
print(f"Original position: {alien_0['x_pos']}")
#Move the alien to the right.
#Determine how far to move the alien based on its current speed.

#alien_0['speed'] = 'slow'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
#The new position is the old position plus the increment.
alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print(f"New position: {alien_0['x_pos']}")
print()

alien_0 = {'color': 'green',
           'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
