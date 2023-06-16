guest_list = ['Jesus', 'St. Peter', 'St. Paul', 'St. James the Greater', 'St. James the Lesser', 'St. John', 'St. Matthew', 'St. Philip', 'St. Andrew', 
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