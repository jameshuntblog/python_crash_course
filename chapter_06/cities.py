# cities.py

phoenix = {'country':'united states','population':1608139,'fact':'The area of '\
    'the city is 500 square miles'}
rome = {'country':'Italy','population':2860009,'fact':'Modern Rome has 280 '\
    'fountains and more than 900 churches.'}
paris = {'country':'France','population':2165423,'fact':'The Eiffel Tower was '\
    'supposed to be a temporary installation, intended to stand for 20 years '\
    'after being built for the 1889 World Fair.'}

cities = {'Phoenix':phoenix,'Rome':rome,'Paris':paris}

for city,city_fact in cities.items():
    print(f"\nCity name: {city}")
    country = city_fact['country']
    population = city_fact['population']
    fact = city_fact['fact']
    print(f"Country: {country.title()}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")