alien_0 = {'color': 'green',
           'points': 5}
alien_1 = {'color': 'yellow',
           'points': 10}
alien_2 = {'color': 'red',
           'points': 15}
alien_3 = {'color': 'black',
           'points': 25,
           'speed': 'fast'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
    
#more realistic aproach
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 
                 'points': 5, 
                 'speed': 'slow'}
    aliens.append(new_alien)

#show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created.
print(f'Total number of aliens: {len(aliens)}')

#change first 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
#show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
