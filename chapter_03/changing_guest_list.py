# changing_guest_list.py

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