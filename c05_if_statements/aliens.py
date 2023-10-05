alien_color = 'green'

if alien_color == 'green':
    print("You've earned 5 points")

if alien_color == 'yellow':
    print("You lose")

#5-4
if alien_color == 'green':
    print("You've earned 5 points")
else:
    print("You've earned 10 points")
    
#5-5
if alien_color == 'green':
    print("You've earned 5 points")
elif alien_color == 'yellow':
    print("You've earned 10 points")
elif alien_color == 'red':
    print("You've earned 15 points")
else:
    print("You Lose!")
    
#5-6
age = 35
if age < 2:
    print("You are baby")
elif age < 4:
    print("You are toddler")
elif age < 13:
    print("You are kid")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are an elder")
