filename = '../files/resons.txt'

with open(filename, 'a') as my_file:
    while True:
        reason = input("Enter a reason or 'q' to stop: ")
        if reason == 'q':
            break
        my_file.write(reason + '\n')
