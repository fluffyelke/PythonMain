#5-8, #5-9
usernames = ['admin', 'vanya', 'elinna', 'alaina', 'veronica']
if usernames:
    for name in usernames:
        if name == 'admin':
            print(f"Hello {name.title()}, would you like to see a status report")
        else:    
            print(f"Greetings {name.title()}. Welcome back!")
else:
    print("We need to find some users!")

#5-10
current_users = usernames[:]
new_users = ['Vanya', 'dawson', 'Caprice', 'Elinna']
temp_new_users = [name.upper() for name in new_users]
for user in current_users:
    if user.upper() in temp_new_users:
        print(f"User name {user} is already taken. Please choose another.")
    else:
        print(f"User name {user} is avaible.")
        
#5-11
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
