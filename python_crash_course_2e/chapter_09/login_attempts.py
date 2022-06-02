# login_attempts.py

class User:
    """A simple attempt to model a software user."""
    def __init__(self, first_name, last_name, age, country, language):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.language = language
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user’s information."""
        print(f"\nThe user's first name is {self.first_name.title()}.")
        print(f"The user's last name is {self.last_name.title()}.")
        print(f"The user's full name is {self.first_name.title()} "\
            f"{self.last_name.title()}.")
        print(f"The user is {self.age} years old.")
        print(f"The user lives in {self.country.title()}.")
        print(f"The user's preferred language is {self.language.title()}.")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"\nHello, {self.first_name.title()} {self.last_name.title()}.")

    def set_login_attempts(self, login_attempts):
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        """Increment login attempts attribute by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print(f"There have been {self.login_attempts} login attempts using "\
            f"{self.first_name.title()} {self.last_name.title()}.")

user_one = User('James', 'Hunt', 39, 'United States', 'English (U.S.)')
user_one.describe_user()
user_one.greet_user()
print(f"Login attempts: {user_one.login_attempts}")
user_one.increment_login_attempts()
print(f"Login attempts: {user_one.login_attempts}")
user_one.increment_login_attempts()
print(f"Login attempts: {user_one.login_attempts}")
print(f"Resetting login attempts...")
user_one.reset_login_attempts()
print(f"Login attempts: {user_one.login_attempts}")

user_one = User('Laser', 'Hunt', 14, 'United States', 'Dog Barking')
user_one.describe_user()
user_one.greet_user()

user_one = User('Bella', 'Hunt', 14, 'United States', 'Dog Barking')
user_one.describe_user()
user_one.greet_user()

user_one = User('Shannon', 'Hunt', 5, 'United States', 'Dog Barking')
user_one.describe_user()
user_one.greet_user()