# three_exits.py

# movie_tickets.py (version one)
# Using a conditional test in the while statement to stop the loop.

# prompt = "\nWelcome to the movie theater!"
# prompt += "\nWe price our tickets based on age."
# prompt += "\nPlease enter your age to determine your ticket price (numbers "\
# "only):"
# prompt += "\nEnter 'quit' to end the program. "

# age = ""

# while age != 'quit':
#     age = input(prompt)
#     if age == 'Quit':
#         break
#     else:
#         try:
#             val = int(age)
#         except ValueError:
#             print("\nThe value you entered is not an integer. Please try again "
#                 "(integers only):")
#             continue
#         else:
#             age = int(age)
#             if age < 3:
#                 print("\nYour ticket is free.")
#             elif age < 13:
#                 print("\nYour ticket is $10.")
#             else:
#                 print("\nYour ticket is $15.")

# movie_tickets.py (version two)
# Use an active variable to control how long the loop runs.

# prompt = "\nWelcome to the movie theater!"
# prompt += "\nWe price our tickets based on age."
# prompt += "\nPlease enter your age to determine your ticket price (numbers "\
# "only):"
# prompt += "\nEnter 'quit' to end the program. "

# age = ""
# active = True

# while active == True:
#     age = input(prompt)
#     if age == 'quit':
#         active = False
#         continue
#     else:
#         try:
#             val = int(age)
#         except ValueError:
#             print("\nThe value you entered is not an integer. Please try again "
#                 "(integers only):")
#             continue
#         else:
#             age = int(age)
#             if age < 3:
#                 print("\nYour ticket is free.")
#             elif age < 13:
#                 print("\nYour ticket is $10.")
#             else:
#                 print("\nYour ticket is $15.")

# movie_tickets.py (version three)
# Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nWelcome to the movie theater!"
prompt += "\nWe price our tickets based on age."
prompt += "\nPlease enter your age to determine your ticket price (integers "\
            "only):"
prompt += "\nEnter 'quit' to end the program. "

age = ""

while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        break
    else:
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