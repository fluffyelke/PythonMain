import json

filename = 'numbers.json'
with open(filename) as my_file:
    numbers = json.load(my_file)
    
print(numbers)
