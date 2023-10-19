#7-1
prompt = "What car would you like to rent? "
car = input(prompt)

print(f"Let me see if i can find you a {car.title()}.")


#7-2
prompt = "How many people are with you? "
peoples = int(input(prompt))

if peoples > 8:
    print("You will have to wait a while.")
else:
    print("Your table is ready")
    
#7-3
prompt = "Please input an number: "
number = int(input(prompt))

if number % 10 == 0:
    print("The number is multiple of 10")
else:
    print("The number is NOT multiple of 10")
