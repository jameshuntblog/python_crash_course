# favorite_numbers.py

favorite_numbers = {'James':9,'Duke':12,'John':29,'Kathleen':56,'Laser':16}
print(f"James's favorite number is {favorite_numbers['James']}.")
print(f"Duke's favorite number is {favorite_numbers['Duke']}.")
print(f"John's favorite number is {favorite_numbers['John']}.")
print(f"Kathleen's favorite number is {favorite_numbers['Kathleen']}.")
print(f"Laser's favorite number is {favorite_numbers['Laser']}.")

favorite_numbers = {'James':[9,18,27,36],'Duke':[12,24,36,42],
    'John':[29,58,87,116],'Kathleen':[56,112,168,224],'Laser':[16,32,48,64]}
for person,favorite_number_list in favorite_numbers.items():
    print(f"\n{person}'s favorite numbers are:")
    for favorite_number in favorite_number_list:
        print(f"\t{favorite_number}")