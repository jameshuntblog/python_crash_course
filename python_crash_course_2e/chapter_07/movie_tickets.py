# movie_tickets.py

prompt = "\nWelcome to the movie theater!"
prompt += "\nWe price our tickets based on age."
prompt += "\nPlease enter your age to determine your ticket price (numbers "\
"only):"
prompt += "\nEnter 'quit' to end the program. "

age = ""

while age != 'quit':
    age = input(prompt)
    try:
        val = int(age)
    except ValueError:
        print("\nThe value you entered is not an integer. Please try again "
            "(integers only):")
        continue
    else:
        age = int(age)
        if age < 3:
            print("\nYour ticket is free.")
        elif age < 13:
            print("\nYour ticket is $10.")
        else:
            print("\nYour ticket is $15.")