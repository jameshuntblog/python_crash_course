# ice_cream_stand.py

class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"\nThe restaurant is called {self.restaurant_name.title()}.")
        print(f"The restaurant specializes in {self.cuisine_type.title()} "\
            "cuisine.")

    def open_restaurant(self):
        """Announce that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is open.")

# # Make an instance called restaurant.
# restaurant = Restaurant("Le Cigar Volant","French")

# # Print the two attributes individually.
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# # Call both methods in the class for the instance.
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# # Create two additional instances of the class.
# restaurant_two = Restaurant("Chez Henri","French")
# restaurant_three = Restaurant("Cheers","Bar")

# # Call describe_restaurant() for each instances.
# restaurant.describe_restaurant()
# restaurant_two.describe_restaurant()
# restaurant_three.describe_restaurant()

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate","Mint Chocolate Chip"]

    def display_flavors(self):
        """Simulate a list of flavors that an ice cream stand sells."""
        print("\nWe proudly serve the following flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor}")

my_ice_cream_stand = IceCreamStand("James's Cone-a-rama","Ice Cream")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()