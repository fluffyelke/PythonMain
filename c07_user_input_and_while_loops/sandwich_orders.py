sandwich_orders = []

while True:
    sandwich = input("\nEnter a sanwdich: ")
    
    sandwich_orders.append(sandwich)
    flag = input("Would you want to stop? (yes/no)? ")
    if flag == 'yes':
        break;
    
finished_sandwiched = []
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiched.append(order)
    
while 'pastrami' in finished_sandwiched:
    finished_sandwiched.remove('pastrami')

print(finished_sandwiched)
