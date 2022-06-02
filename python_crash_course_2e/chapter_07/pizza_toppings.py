# pizza_toppings.py

prompt = "\nEnter your desired pizza topping:"
prompt += "\nEnter 'quit' to end the program. "

topping = ""

while topping != 'quit':
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"\nWe’ll add {topping} to your pizza!")

