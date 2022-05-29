# dog.py

class Dog:
    # The text below is a "doctring which describes what the class 
    # does."
    """A simple attempt to model a dog."""

    # The __init__ method is a special method that Python runs 
    # automatically whenever a new instance of the class is created.
    
    # The __init__() method is being defined with three parameters, 
    # self, name and age.
    
    # The self parameter is required in the method definition, and 
    # it must come first before the other parameters.

    # Every method call associated with an instance automatically 
    # passes self, which is a reference to the instance itself; it 
    # gives the individual instance access to the attributes and 
    # methods of the class.

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # The two variables defined below each have the prefix self.
        # Any variable prefixed with self is available to every 
        # method in the class, and we'll also be able to access 
        # these variables through any instance created from the 
        # class.
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

dog_library = {'Willie':6,'Lucy':3,'Laser':14,'Bella':14}

for name, age in dog_library.items():
    dog_instance = Dog(name, age)
    print(f"\nMy dog's name is {dog_instance.name}.")
    print(f"My dog is {dog_instance.age} years old.")
    dog_instance.sit()
    dog_instance.roll_over()
