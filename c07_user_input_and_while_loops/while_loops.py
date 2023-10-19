count = 1
while count <= 5:
    print(count)
    count += 1
    
prompt = "\nTell me something, and I will reapeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
