# lottery.py

from random import choice

numbers_and_letters = [9,15,31,42,8,11,4,7,23,45,'J','A','M','E','S']

winning_ticket = [choice(numbers_and_letters), choice(numbers_and_letters)\
, choice(numbers_and_letters), choice(numbers_and_letters)]
print(f"Any ticket matching these four numbers or letters wins a prize: "\
    f"{winning_ticket}.")

ticket = []
number_of_attempts = 0

while winning_ticket != ticket:
    ticket = [choice(numbers_and_letters), choice(numbers_and_letters), \
    choice(numbers_and_letters), choice(numbers_and_letters)]
    number_of_attempts += 1
    print(number_of_attempts)

print(ticket)
print(f"The loop had to run {number_of_attempts} to give you a winning ticket.")

