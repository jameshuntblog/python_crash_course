# cars.py

def make_car(manufacturer,model_name,**kwargs):
    """Build a dictionary containing everything we know about a user."""
    kwargs['make'] = manufacturer
    kwargs['model'] = model_name
    return kwargs

car_info = make_car('ford','mustang',color='red',\
    optional_feature='convertible')

print(car_info)