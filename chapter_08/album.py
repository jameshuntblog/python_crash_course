# album.py

import album_function
from album_function import make_album
from album_function import make_album as ma
import album_function as af
from album_function import*

# def make_album(artist_name,album_title,number_of_songs=None):
#     if number_of_songs:
#        album = {'artist name':artist_name,'album title':album_title,'number '\
#           'of songs':number_of_songs} 
#     else:
#         album = {'artist name':artist_name,'album title':album_title}
#     return album

print(album_function.make_album('Sublime','Sublime',17))
print(album_function.make_album('Adam Sandler','What the Hell Happened to Me?',20))
print(album_function.make_album('Bloodhound Gang','One Fierce Beer Coaster'))

print(make_album('Sublime','Sublime',17))
print(make_album('Adam Sandler','What the Hell Happened to Me?',20))
print(make_album('Bloodhound Gang','One Fierce Beer Coaster'))

print(ma('Sublime','Sublime',17))
print(ma('Adam Sandler','What the Hell Happened to Me?',20))
print(ma('Bloodhound Gang','One Fierce Beer Coaster'))

print(af.make_album('Sublime','Sublime',17))
print(af.make_album('Adam Sandler','What the Hell Happened to Me?',20))
print(af.make_album('Bloodhound Gang','One Fierce Beer Coaster'))
