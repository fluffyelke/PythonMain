import json

filename = 'fav_num3.json'

def write_json(filepath):
    number = input("What is your favorite number? ")
    with open(filepath, 'w') as my_file:
        json.dump(number, my_file)
    return number    
    
def read_json(filepath):
    try:
        with open(filepath) as my_file:
            number = json.load(my_file)
    except FileNotFoundError:
        return None
    else:
        return number

def run_program():
    number = read_json(filename)
    if number:
        print(f"Your favorite number is {number}!")
    else:
        number = write_json(filename)
        print(f"We will record your {number} number!")
    
run_program()
