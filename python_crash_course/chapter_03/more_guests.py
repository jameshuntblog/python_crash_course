# more_guests.py

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