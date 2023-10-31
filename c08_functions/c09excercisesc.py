#8-9
short_messages = ['first message', 'gold go up', 'or may be go down']

def print_messages(my_list):
    """
    Function to print messages.
    """
    for element in my_list:
        print(f"{element}")

print_messages(short_messages)

#8-10
def send_messages(from_list, to_list):
    """
    Move messages from one list to another.
    """
    while from_list:
        text_msg = from_list.pop()
        print(f"Getting: {text_msg}")
        to_list.append(text_msg)

my_new_short_msg_list = []

#send_messages(short_messages, my_new_short_msg_list)
#print_messages(short_messages)
#print_messages(my_new_short_msg_list)


#8-11     #Pass a copy list to the method using my_list[:]
send_messages(short_messages[:], my_new_short_msg_list)
print_messages(short_messages)
print_messages(my_new_short_msg_list)
