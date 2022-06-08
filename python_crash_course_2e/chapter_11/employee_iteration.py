# employee.py

class Employee:
    def __init__(self,first_name,last_name,annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        self.raise_amount = raise_amount
        self.annual_salary += self.raise_amount
        print(f"\nBased on {self.first_name.title()} {self.last_name.title()}"\
            f"'s performance this year, he is receiving a "
            f"{self.raise_amount:,}\nannual salary change.")


employee_one = Employee('jordan','da loser',20000)
print(f"{employee_one.first_name.title()} {employee_one.last_name.title()}'s "\
    f"starting salary was ${employee_one.annual_salary:,} due to his "\
    f"low-level skills \nand the general stench of incompetence that "\
    f"surrounds him.")
employee_one.give_raise(-5000)
print(f"\n{employee_one.first_name.title()} {employee_one.last_name.title()}'s "\
    f"new annual salary will be an appropriately humiliating \n$"\
    f"{employee_one.annual_salary:,}.")