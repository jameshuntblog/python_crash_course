# no_pastrami.py

sandwich_orders = ['tuna','meatball','turkey','chicken salad','pastrami',\
'pastrami','pastrami']
finished_sandwiches = []

print("\nWe received the following sandwich orders:")
for sandwich_order in sandwich_orders:
    print(sandwich_order)

print("\nThe deli has run out of pastrami. All pastrami orders will be "\
    "cancelled and refunded")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order} sandwich.")

    finished_sandwiches.append(sandwich_order)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)