# restaurant.py

class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"\nThe restaurant is called {self.restaurant_name.title()}.")
        print(f"The restaurant specializes in {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Announce that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is open.")

restaurant = Restaurant("Le Cigar Volant","French")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()