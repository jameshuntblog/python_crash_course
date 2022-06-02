# threes.py

threes = []
for value in range(1,31):
	multiple_of_three = value * 3
	threes.append(multiple_of_three)
print(threes)

threes = []
for value in range(1,31):
	threes.append(value * 3)
print(threes)

threes = [value * 3 for value in range(1,31)]
print(threes)