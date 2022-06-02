# restaurant_seating.py

people_in_dinner_group = input("How many people are in your dinner group? ")
people_in_dinner_group = int(people_in_dinner_group)

if people_in_dinner_group > 8:
    print(f"\nThere is a short wait for a dinner group of "\
        f"{people_in_dinner_group}. Please wait in the seats here or at "
        "the bar. \nWe'll notify you when your table is ready.")
else:
    print("\nYour table is ready.")