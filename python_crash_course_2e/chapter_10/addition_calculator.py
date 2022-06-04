# addition_calculator.py

print("\nThis program adds two numbers together.")
while True:
    try:
        print("\nIf you wish to exit the program, please enter 'q' at any time.")
        first_number = input(f"Please input the first number: ")
        if first_number == 'q':
            break
        second_number = input(f"Please input the second number: ")
        if first_number == 'q':
            break
        result = float(first_number) + float(second_number)
        print(f"\nThe result of adding the two numbers is {result}!")
    except ValueError:
        print("\nOne of the inputs you entered is not a valid number!")
