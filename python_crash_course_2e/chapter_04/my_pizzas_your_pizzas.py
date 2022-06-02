# my_pizzas_your_pizzas.py

pizzas = ['sausage and greenpepper','supreme','pepperoni and pineapple']
for pizza in pizzas:
	print(pizza)

pizzas = ['sausage and greenpepper','supreme','pepperoni and pineapple']
for pizza in pizzas:
	print(f"I really enjoy eating {pizza} pizza.")

print("I really love pizza!")

pizzas = ['sausage and greenpepper','supreme','pepperoni and pineapple']
friend_pizzas = pizzas[:]

friend_pizzas.append('meat lovers')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)



