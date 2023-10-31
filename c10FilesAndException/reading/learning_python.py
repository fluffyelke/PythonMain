#10-1
filename = '../files/learning_python.txt'
with open(filename) as my_file:
    contents = my_file.read()

print('\n\nAs whole file')
print(contents.rstrip())

print('\n\nAs Lines')

with open(filename) as my_file:
    for line in my_file:
        print(line.strip())

print("\n\nAs list")
with open(filename) as my_file:
    lines = my_file.readlines()
    
for line in lines:
    print(line.strip())
    
print("\n\nRepalace Python with C")
with open(filename) as my_file:
    lines = my_file.readlines()
for line in lines:
    line = line.replace('Python', 'Cpp')
    print(line.strip())
