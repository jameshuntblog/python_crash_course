# slices.py

magicians = ['alice','david','carolina','jude','Tom']
for magician in magicians:
	print(magician)

print("\nThe first three items in the list are:")
for magician in magicians[:3]:
	print(magician)

print("\nThe three items from the middle of the list are:")
for magician in magicians[1:4]:
	print(magician)

print("\nThe last three items in the list are:")
for magician in magicians[-3:]:
	print(magician)
