#10-7
first = 0
second = 0
while True:
    try:
        first = int(input("Input a number: "))
        second = int(input("Input another number: "))
        result = first + second
        print(result)
    except ValueError:
        print("You enter a non number value")
    
