#9-13
from dice import Die

my_dice = Die()

my_dice.roll_die()

for number in range(1, 11):
    my_dice.roll_die()


print('\n\nTen sides Die\n')
my_dice = Die(10)
my_dice.roll_die()
for number in range(1, 11):
    my_dice.roll_die()
    
print('\n\n 20 sides die\n')
my_dice = Die(20)
for number in range(1, 20):
    my_dice.roll_die()
