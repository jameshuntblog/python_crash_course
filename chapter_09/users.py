# users.py

# Make a class called User.
class User:
    """A simple attempt to model a software user."""
    def __init__(self, first_name, last_name, age, country, language):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.language = language

    # Make a method called describe_user() that prints a summary of the user's
    # information
    def describe_user(self):
        """Prints a summary of the user’s information."""
        print(f"\nThe user's first name is {self.first_name.title()}.")
        print(f"The user's last name is {self.last_name.title()}.")
        print(f"The user's full name is {self.first_name.title()} "\
            f"{self.last_name.title()}.")
        print(f"The user is {self.age} years old.")
        print(f"The user lives in {self.country.title()}.")
        print(f"The user's preferred language is {self.language.title()}.")

    # Make a method called greet_user() that prints a personalized greeting to
    # the user.
    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"\nHello, {self.first_name.title()} {self.last_name.title()}.")

# Create several instances representing different users, and call both methods
# for each user.
user_one = User('James', 'Hunt', 39, 'United States', 'English (U.S.)')
user_one.describe_user()
user_one.greet_user()

user_two = User('Laser', 'Hunt', 14, 'United States', 'Dog Barking')
user_two.describe_user()
user_two.greet_user()

user_three = User('Bella', 'Hunt', 14, 'United States', 'Dog Barking')
user_three.describe_user()
user_three.greet_user()

user_four = User('Shannon', 'Hunt', 5, 'United States', 'Dog Barking')
user_four.describe_user()
user_four.greet_user()

users = {'id_numbers':[0,1,2,3],'first_names':['James','Laser','Bella',\
'Shannon'],'last_names':['Hunt','Hunt','Hunt','Hunt'],'ages':[39,14,14,5],\
'countries':['United States','United States','United States','United States']\
,'languages':['English (U.S.)','Dog Barking','Dog Barking','Dog Barking']}

for id_number,first_name,last_name,age,country,language in \
zip(users['id_numbers'],users['first_names'], users['last_names'], \
    users['ages'],users['countries'] ,users['languages']):
    current_user = User(first_name,last_name,age,country,language)
    current_user.describe_user()
    current_user.greet_user()