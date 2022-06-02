# number_served.py

class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"\nThe restaurant is called {self.restaurant_name.title()}.")
        print(f"The restaurant specializes in {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Announce that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is open.")

    def read_number_served(self):
        """Print a statement showing the number of customers served."""
        print(f"This restaurant has served {self.number_served} customers.")

    def set_number_served(self, number_served):
        """
        Set the number served to the given value.
        """
        self.number_served = number_served

    def increment_number_served(self, additional_customers_served):
        self.number_served += additional_customers_served

restaurant = Restaurant("Le Cigar Volant","French")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.read_number_served()
restaurant.describe_restaurant()
restaurant.open_restaurant
restaurant.set_number_served(25)
restaurant.read_number_served()
restaurant.increment_number_served(5)
restaurant.read_number_served()
restaurant.increment_number_served(5)
restaurant.read_number_served()