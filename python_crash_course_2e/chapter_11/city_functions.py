# city_country.py

def get_formatted_city_country(city,country,population=''):
    """Funciton that accepts two parameters, city name and country name."""
    if population:
        city_country_string = f"{city}, {country} – population {population}"
    else:
        city_country_string = f"{city}, {country}"
    return city_country_string.title()