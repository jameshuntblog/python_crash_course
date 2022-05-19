# people.py

person_one = {'first_name':'Nicholas','last_name':'Pomeroy','age':21,
    'city':'Geneva'}
person_two = {'first_name':'Dylan','last_name':'Pierpont','age':40,
    'city':'Dublin'}
person_three = {'first_name':'Hafþór','last_name':'Björnsson ','age':33,
    'city':'Reykjavík'}

people = [person_one,person_two,person_three]

for person in people:
    print(f"\nFirst name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Full name: {person['first_name']} {person['last_name']}")
    print(f"City: {person['city']}")
    print(f"Age: {person['age']}")