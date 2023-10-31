#write to an empty file using 'w' flag
filename = '../files/programming.txt'
with open(filename, 'w') as my_file:
    my_file.write('I love programming.\n')
    my_file.write(str([1, 2, 3, 4, 5, 6, 7]))
    my_file.write('\n')

#open and append
with open(filename, 'a') as my_file:
    my_file.write('I also love finding meaning in large datasets.\n')
    my_file.write('I love creating apps that can run in a browser.\n')
