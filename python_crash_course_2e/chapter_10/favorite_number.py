# favorite_number.py

import json

# This is a program that prompts for the user's favorite number.

filename = 'favorite_number.json'

with open(filename, 'w') as f:
    favorite_number = input("Please input your favorite number: ")
    json.dump(favorite_number, f)