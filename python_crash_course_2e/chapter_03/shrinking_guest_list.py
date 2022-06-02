# shrinking_guest_list.py

guest_list = ['Georgia','Elizabeth','Ina','Kathleen']
message = f"Hi {guest_list[0].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[1].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[2].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[3].title()}, I would like you to join me at dinner this coming Friday."
print(message)
print("\nIna couldn't make it because she had to work.")
guest_list.remove("Ina")
guest_list.append("John")
message = f"Hi {guest_list[0].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[1].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[2].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[3].title()}, I would like you to join me at dinner this coming Friday."
print(message)

print("\nI just found a bigger dinner table for our dinner on Friday.\n")

guest_list.insert(0,'Mike')
guest_list.insert(3,'Tom')
guest_list.append('Duke')

message = f"Hi {guest_list[0].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[1].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[2].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[3].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[4].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[5].title()}, I would like you to join me at dinner this coming Friday."
print(message)
message = f"Hi {guest_list[6].title()}, I would like you to join me at dinner this coming Friday."
print(message)

message = "\nSorry, I just discovered that my new dinner table will not arrive in time. I can only invite two people for dinner."
print(message)
last_guest = guest_list.pop()
print(f"Hi {last_guest}, I am unable to invite you to dinner this time. My sincerest apologies. I will be sure to include you on future invites once my new table arrives.")
last_guest = guest_list.pop()
print(f"Hi {last_guest.title()}, I am unable to invite you to dinner this time. My sincerest apologies. I will be sure to include you on future invites once my new table arrives.")
last_guest = guest_list.pop()
print(f"Hi {last_guest.title()}, I am unable to invite you to dinner this time. My sincerest apologies. I will be sure to include you on future invites once my new table arrives.")
last_guest = guest_list.pop()
print(f"Hi {last_guest.title()}, I am unable to invite you to dinner this time. My sincerest apologies. I will be sure to include you on future invites once my new table arrives.")
last_guest = guest_list.pop()
print(f"Hi {last_guest.title()}, I am unable to invite you to dinner this time. My sincerest apologies. I will be sure to include you on future invites once my new table arrives.")
print(guest_list)
print(f"Hi {guest_list[0].title()}, I wanted to let you know that I needed to adjust my guest list due to my new table not arriving on time, but I wanted to confirm that you are still invited to my dinner party.")
print(f"Hi {guest_list[1].title()}, I wanted to let you know that I needed to adjust my guest list due to my new table not arriving on time, but I wanted to confirm that you are still invited to my dinner party.")

del guest_list[0]
del guest_list[0]
print(guest_list)
