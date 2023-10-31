from random import randint
import collections
#9-14
lottery_list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l']
print(lottery_list)
lottery_result = []
print(len(lottery_list))
for elem in range(0, 5):
    value = lottery_list.pop(randint(0, len(lottery_list) - 1))
    lottery_result.append(value)
    
print(lottery_list)
print(lottery_result)

my_ticket = []
count = 0
while True:
    lottery_list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l']
    count += 1
    for elem in range(0, 5):
        value = lottery_list.pop(randint(0, len(lottery_list) - 1))
        my_ticket.append(value)
    if collections.Counter(lottery_result) == collections.Counter(my_ticket):
        break
    else:
        my_ticket.clear()

print(f"Total Attempts to win a lottery: {count}") 
print(my_ticket)
