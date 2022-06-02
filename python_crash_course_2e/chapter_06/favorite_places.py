# favorite_places.py

favorite_places = {
    'james':['Acadia National Park','Maine Wildlife Park','Coastal Maine Botanical Gardens'],
    'georgia':['Bangor City Forest','Round1 Bowling & Amusement','Maine Discovery Museum'],
    'ina':['Paris','Washington D.C.','Charlottesville'],
    }

for person,places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")