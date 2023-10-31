#8-6
def city_country(city, country):
    """
    Function that return the city and the country.
    """
    location = {"city": city,
                "country": country}
    return location

city = city_country('sofia', 'bulgaria')
print(city)

city = city_country('moscow', 'russia')
print(city)

city = city_country('london', 'england')
print(city)

def make_album(artist, album, songs = None):
    """
    Function to build a dictionary of a artist and album.
    """
    if songs:
        vinyl = {'artist': artist,
                 'album': album,
                 'songs': songs}
    else:
        vinyl = {'artist': artist,
                 'album': album}
    return vinyl
vinyl_1 = make_album('burzum', 'hvys lyset tar oss', 10)
vinyl_2 = make_album('alizee', 'mes courants electriques')
vinyl_3 = make_album('judas priest', 'british steel')
print(vinyl_1, "\n", vinyl_2, "\n", vinyl_3)


#8-8
def user_input():
    """
    Get Input from the user and make an album
    """
    while True:
        artist = input("\nInput artist name or 'q' to stop: ")
        if artist == 'q':
            break
        album = input("\nInput album name or 'q' to stop: ")
        if album == 'q':
            break
        curr_input = make_album(artist, album)
        print("You Enter: ", curr_input)

user_input()
