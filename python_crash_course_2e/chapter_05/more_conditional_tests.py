# more_conditional_tests.py

# Tests for equality and inequality with strings
test_string = 'Do you like Piña Coladas?'
print(test_string == 'Do you like Piña Coladas?')
print(test_string != 'Do you like pina coladas?')
print(test_string == 'Do you like pina coladas?')

# Tests using the lower() method
test_string_two = 'Gary Paulson wrote the novel Hatchet.'
print(f"\n{test_string_two == 'gary paulson wrote the novel hatchet.'}")
print(test_string_two.lower() == 'gary paulson wrote the novel hatchet.')
print(test_string_two.lower() == 'Gary Paulson wrote the novel Hatchet.')

number = 5
print(f"\n{number == 5}")
print(number >= 5)
print(number <= 5)
print(number != 5)
print(number == 5 and number >=5 and number <=5)
print(number <5 or number >5 or number == 5)

test_list = ['snake','rat','cat','dog']
print(f"\n{'snake' in test_list and 'rat' in test_list}")
print(f"{'snake' in test_list or 'panda' in test_list}")

test_list = ['snake','rat','cat','dog']
print(f"\n{'panda' not in test_list}")
print(f"{'snake' not in test_list}")