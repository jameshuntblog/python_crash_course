"""Model an administrative user."""

# admin.py

from users import User

class Admin(User):

    def __init__(self, first_name, last_name, age, country, language):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an admin.
        """
        
        super().__init__(first_name, last_name, age, country, language)
        self.privileges = ["can add post", "can delete post", "can ban user", \
        "can embezzle funds"]

    def show_privileges(self):
        """Simulate a list of privileges that an admin would have."""
        print("You have the following privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")