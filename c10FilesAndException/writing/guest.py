filename = "../files/guest_book.txt"


    
with open(filename, 'a') as my_file:
    value = 0
    while True: 
        if value == 5:
            break
        name = input('Please enter your name: ')
        print(f"Greetings {name.title()}.")
        my_file.write(f"{name.title()} has visit the site.\n")
        value += 1
        


