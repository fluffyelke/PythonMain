for value in range(1, 6):
    print(value)

#create a list
numbers = list(range(10))
print(numbers)

#skip with step
even_numbers = list(range(2, 21, 2))
print(even_numbers)

#square numbers
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

#min / max / sum
digits = list(range(10))
print(f"min: ", min(digits))
print(f"max: ", max(digits))
print(f"sum: ", sum(digits))
