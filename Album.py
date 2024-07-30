def make_album(artist_name, album_title, number_of_tracks = ""):
    if number_of_tracks:
        album_info = {'name' : artist_name, 'title' : album_title, 'track-number' : number_of_tracks}
    else:
        album_info = {'name' : artist_name, 'title' : album_title}


    return album_info
#album = make_album("Flavour", "Lovely", "5")
#print(album)
albums = []
while True:
    artist = input("What is the name of your artist? \ntype q to quit at anytime")
    if artist == "q":
        break
    album = input("What is the name of their album?")
    if album == "q":
        break
    tracks = input("how many tracks do they have?")
    if tracks == "q":
        break

    album = make_album(artist,album,tracks)
    albums.append(album)

    #print(album)
    continue
print(albums)

