import json
import random
numbers = [random.randrange(1, 100, 1) for num in range(1, 100)]


filename = 'numbers.json'
with open(filename, 'w') as my_file:
    json.dump(numbers, my_file)
