# pets.py

laser = {'name':'Laser','species':'dog','owner':'James Hunt',}
shannon = {'name':'Shannon','species':'dog','owner':'James Hunt',}
bonnie = {'name':'Bonnie','species':'dog','owner':'John Hunt',}
vanna = {'name':'Vanna','species':'dog','owner':'John Hunt',}
kitty = {'name':'Kitty','species':'cat','owner':'John Hunt',}

pets = [laser,shannon,bonnie,vanna,kitty]

for pet in pets:
    print(f"\nName: {pet['name']}")
    print(f"Species: {pet['species']}")
    print(f"Owner: {pet['species']}")