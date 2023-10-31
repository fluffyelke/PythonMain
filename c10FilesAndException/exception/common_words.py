#10-10
def count_words(filepath, key_word):
    """
    Count how many times a word is in a file.
    """
    try:
        with open(filepath, encoding = 'utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"File {filepath} was not found!")
    else:
        count = contents.lower().count(key_word)
        print(f"There are {count} occurences of word {key_word} in the file {filepath}.")


filenames = ['../files/alice.txt', '../files/moby_dick.txt', '../files/little_women.txt']
for files in filenames:
    print(count_words(files, "caprice"))
