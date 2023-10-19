#6-5
rivers_location = {'nile': 'egypt',
                   'amazon': 'brazil',
                   'iskar': 'bulgaria'}
for river, country in rivers_location.items():
    print(f"The {river.title()} runs through {country.title()}.")
for river in rivers_location:
    print(river)
for river in rivers_location:
    print(rivers_location[river])
