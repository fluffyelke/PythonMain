#3-4
guests = ['vanya', 'elinna', 'caprice']
for name in guests:
    print(f"Would you join me for a dinner, {name.title()}?")

#3-5
print(f"Unofortunately {guests[1].title()} wont be able to come.")

del guests[1]
guests.insert(1, 'alaina')

for name in guests:
    print(f"Would you join me for a dinner, {name.title()}?")
    
#3-6
print(f"We found a bigger place for a diiner")
guests.insert(0, 'deska')
guests.insert(2, 'iva')
guests.append('stefi')
for name in guests:
    print(f"Would you join me for a dinner, {name.title()}?")

#3-7
print("\nTotal Guests: ", end = '')
print(len(guests))
print(f"We can invite only 2 people now...")
guests.pop()
guests.pop(0)
guests.pop(1)
guests.pop(1)
for name in guests:
    print(f"Would you join me for a dinner, {name.title()}?")
    
del guests[-1]
del guests[0]
print(guests)
