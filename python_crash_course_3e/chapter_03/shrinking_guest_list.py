guest_list = ['The Blessed Virgin Mary', 'St. Peter', 'St. Paul', 'St. James the Greater', 'St. James the Lesser', 'St. John', 'St. Matthew', 'St. Philip', 'St. Andrew', 
              'St. Bartholomew or Nathanael', 'St. Thomas', 'St. Thaddeus', 'St. Simon']

for guest in guest_list:
    print(f"Dear {guest}, Please come to my house for dinner on July 10th at 7:30 pm. We will be serving a delicous fish chowder!")

unable_to_attend = 'St. Simon'
print(f"Unfortunately, {unable_to_attend} is unable to attend the dinner.")

guest_list.remove(unable_to_attend)

replacement_invitation = 'St. Matthias'

print(f"{replacement_invitation} has been invited to fill {unable_to_attend}'s seat.")

guest_list.append(replacement_invitation)

for guest in guest_list:
    print(f"Dear {guest}, Please come to my house for dinner on July 10th at 7:30 pm. We will be serving a delicous fish chowder!")

print("We found a larger table for the party, so we are inviting more guests!")

additional_guest_one = 'Jesus'
additional_guest_two = 'Mary Magdalene'
additional_guest_three = 'Cleopas'

guest_list.insert(0, additional_guest_one)
guest_list.insert(6, additional_guest_two)
guest_list.append(additional_guest_three)

for guest in guest_list:
    print(f"Dear {guest}, Please come to my house for dinner on July 10th at 7:30 pm. We will be serving a delicous fish chowder!")

while len(guest_list) > 2:
    guest_uninvited = guest_list.pop()
    print(f"Dear {guest_uninvited}, I am so sorry, but I was anticipating the arrival of a large table for my upcoming party. Unfortunately, the table will not arrive in time, so I am unable to accomodate you.")

for guest in guest_list:
    print(f"Dear {guest}, Please come to my house for dinner on July 10th at 7:30 pm. We will be serving a delicous fish chowder! I still have room for you.")

del guest_list[0]
del guest_list[0]

print(guest_list)