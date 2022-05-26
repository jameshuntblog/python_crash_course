# album_function.py

def make_album(artist_name,album_title,number_of_songs=None):
    if number_of_songs:
       album = {'artist name':artist_name,'album title':album_title,'number of '
       'songs':number_of_songs} 
    else:
        album = {'artist name':artist_name,'album title':album_title}
    return album