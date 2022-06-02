# extensions.py

phoenix = {'country':'united states','population':1608139,'fact':'The area of '\
    'the city is 500 square miles','favorite_place':'Chase Field'}
rome = {'country':'Italy','population':2860009,'fact':'Modern Rome has 280 '\
    'fountains and more than 900 churches.','favorite_place':'the Colosseum'}
paris = {'country':'France','population':2165423,'fact':'The Eiffel Tower was '\
    'supposed to be a temporary installation, intended to stand for 20 years '\
    'after being built for the 1889 World Fair.','favorite_place':'the Notre Dame Cathedral'}

cities = {'Phoenix':phoenix,'Rome':rome,'Paris':paris}

for city,city_fact in cities.items():
    print(f"\nCity name: {city}")
    country = city_fact['country']
    population = "{:,}".format(city_fact['population'])
    fact = city_fact['fact']
    favorite_place = city_fact['favorite_place']
    print(f"Country: {country.title()}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")
    print(f"My favorite place in {city} is {favorite_place}.")