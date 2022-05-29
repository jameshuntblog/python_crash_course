# electric_car.py

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing a car's mileage."""
        print(f"This car has a {'{:,}'.format(self.odometer_reading)} miles "\
            "on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
         """Simulate filling the car's tank with gas."""
         print(f"This {self.make.title()} {self.model.title()} is now filled with gas.")

class Battery:
    """A simple attempt to model a battery for an electic car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an electric car.
        """
        
        super().__init__(make, model, year)
        # Commented out code from previous iteration of the program.
        # self.battery_size = 75
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print(f"{self.make.title()} {self.model.title()} electric vehicles "\
            "do not have a gas tank!")

    # Commented out code from previous iteration of the program.
    # def describe_battery(self):
    #     """Print a statement describing the battery size."""
    #     print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model S', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# my_mustang = Car('Ford', 'Mustang', 1992)
# print(my_mustang.get_descriptive_name())
# my_mustang.fill_gas_tank()
# my_mustang.update_odometer(150_000)
# my_mustang.read_odometer()