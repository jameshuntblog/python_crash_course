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

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
    print(f"Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print(f"Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms','olives','green peppers','pepperoni','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")