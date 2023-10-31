#read whole file
with open('../files/pi_digits.txt') as my_file:
    contents = my_file.read()
    print(contents.rstrip())
print(contents)


#read line by line
filename = "../files/pi_digits.txt"
with open(filename) as my_file:
    for line in my_file:
        print(line.rstrip())    #to remove each blank line in the file.
        
#store contents of a file into a list
with open(filename) as my_file:
    lines = my_file.readlines()
print(lines)    
for line in lines:
    print(line.rstrip())
    
    
#working with a files contents
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
