# addition.py

try:
    print("This program adds two numbers together.")
    first_number = input(f"Please input the first number: ")
    second_number = input(f"Please input the second number: ")
    result = float(first_number) + float(second_number)
    print(f"The result of adding the two numbers is {result}!")
except ValueError:
    print("\nOne of the inputs you entered is not a valid number!")
