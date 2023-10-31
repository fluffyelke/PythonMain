def get_formatted_name(first_name, last_name):
    """
    Return a full name, neatly formatted.
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('vanya', 'dimitrova')
print(musician)


#optional argument
def get_formatted_name_optional(first_name, last_name, middle_name = ''):
    """
    Return a full name, neatly formatted.
    """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_optional('john', 'hooker', 'lee')
print(musician)

other_musician = get_formatted_name_optional('jimi', 'hendrix')
print(other_musician)
