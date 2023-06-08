bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

for bicycle in bicycles:
    print(f"My favorite brand of bicycle is {bicycle.title()}.")

print(bicycles[0:])
print(len(bicycles))