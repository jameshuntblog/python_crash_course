# deli.py

sandwich_orders = ['tuna','meatball','turkey','chicken salad']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order} sandwich.")

    finished_sandwiches.append(sandwich_order)

print("The following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)