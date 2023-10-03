language = '     python   '
language = language.rstrip()
print(language)

language = '     python   '
language = language.lstrip()
print(language)


language = '     python   '
language = language.strip()
print(language)


#2-3
person_name = 'vanya'
print(f"Hellp {person_name.title()} would you like to learn some python today")

person_name = 'elinna'
print(person_name.lower())
print(person_name.upper())
print(person_name.title())

person = 'albert einstein'
quote = 'once said, "A person who never made a mistake never tried anything new"'
print(f"{person.title()} {quote}")

person = "\t\n\n\tveronica\t\tmars\n\t"
print(person.lstrip())
print(person.rstrip())
print(person.strip())
