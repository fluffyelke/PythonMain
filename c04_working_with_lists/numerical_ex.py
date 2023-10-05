#4-3
print(list(range(1, 21)))

#4-4
numbers = list(range(1, 1000))
print(numbers)

#4-5
print(f"min: ", min(numbers))
print(f"max: ", max(numbers))
print(f"sum: ", sum(numbers))


#4-6
#odd numbers
print(list(range(1, 21, 2)))

numbers = list(range(1, 21, 2))
for num in numbers:
    print(num, end = ' ')
print()
#4-7
print(list([value ** 3 for value in range(3, 31)]))     #list comprehension
print([value ** 3 for value in range(3, 31)])       #shorter variant
#and another alternative
numbers = [value ** 3 for value in range(3, 30)]
for num in numbers:
    print(num, end = ' ')
print()
#and another example
for num in [value ** 3 for value in range(3, 30)]:
    print(num, end = ' ')
print()
