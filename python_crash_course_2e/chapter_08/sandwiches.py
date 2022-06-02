# sandwiches.py

def sandwich_items(*items):
    print("You ordered the following items on your sandwich:")
    for item in items:
        print(item)

sandwich_items("Turkey","Cheddar cheese","Tomato","Mayo","Bacon")
sandwich_items("Turkey","Cheddar cheese","Tomato")
sandwich_items("Turkey")