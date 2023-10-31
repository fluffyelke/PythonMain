filename = '../files/alice.txt'

def count_words(filename):
    """
    Count the approximate number of words in a file.
    """
    try:
        with open(filename, encoding = 'utf-8') as my_file:
            contents = my_file.read()
            #print(contents)
    except FileNotFoundError:
        #pass
        print(f"Sorry, the file {filename} does not exist.")
        #we can simple use keyword pass, to not show the exception
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
#title = 'Alice in Wonderland'
#print(title.split())

count_words(filename)

filenames = ['../files/sidhartha.txt', '../files/moby_dick.txt', '../files/little_women.txt']
for files in filenames:
    count_words(files)
    
