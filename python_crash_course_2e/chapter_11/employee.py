# employee.py

class Employee:
    """
        Create a employ and a set of responses for use in all test methods.
        """
    def __init__(self,first_name,last_name,annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        self.raise_amount = raise_amount
        self.annual_salary += self.raise_amount
