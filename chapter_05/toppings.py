# toppings.py

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms','onions','pineapple']

if 'mushrooms' in requested_toppings:
    print("The pizza includes mushrooms.")

if 'pepperoni' in requested_toppings:
    print("The pizza includes pepperoni.")
else:
    print("The pizza does not include pepperoni.")