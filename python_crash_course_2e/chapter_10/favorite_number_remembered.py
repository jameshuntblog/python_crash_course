# favorite_number_remembered.py

import json

# This is a program that prompts for the user's favorite number.

try:
    with open('favorite_number.json') as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("Please input your favorite number: ")
    with open('favorite_number.json', 'w') as f:
        json.dump(favorite_number, f)
    print(f"We'll remember your favorite number when you come back!")
else:
    print(f"I know your favorite number! It’s {favorite_number}.")