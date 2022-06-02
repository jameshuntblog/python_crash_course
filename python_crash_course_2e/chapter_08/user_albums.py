# user_albums.py

# album.py

def make_album(artist_name,album_title,number_of_songs=None):
    if number_of_songs:
       album = {'artist name':artist_name,'album title':album_title,'number of songs':number_of_songs} 
    else:
        album = {'artist name':artist_name,'album title':album_title}
    return album

while True:
    print("\nPlease provide the album information:")
    print("(enter 'q' at any time to quit)")
    artist_name_input = input("Artist name: ")
    if artist_name_input == 'q':
        break
    album_title_input = input("Album title: ")
    if album_title_input == 'q':
        break
    number_of_songs_input = input("# songs on album (optional--press enter if "\
        "you wish to leave blank): ")
    if number_of_songs_input == 'q':
        break
    print(make_album(artist_name_input,album_title_input,number_of_songs_input))
