#10-8
filenames = ['../files/cats.txt', '../files/somefile.txt', '../files/dogs.txt']

for files in filenames:
    try: 
        with open(files) as file:
            print(file.read())
    except FileNotFoundError:
        #pass    #10-9
        print(f"File {files} not found!")
