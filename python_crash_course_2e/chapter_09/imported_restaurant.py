# imported_restaurant

from restaurant import Restaurant as Res

# Make an instance called restaurant.
restaurant = Res("Le Cigar Volant","French")

# Print the two attributes individually.
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call both methods in the class for the instance.
restaurant.describe_restaurant()
restaurant.open_restaurant()