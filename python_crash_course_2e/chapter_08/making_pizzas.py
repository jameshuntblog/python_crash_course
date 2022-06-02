# making_pizzas.py

import pizza as pz

pz.make_pizza(16,'pepperoni')
pz.make_pizza(12,'mushrooms','green peppers','extra cheese')

# Or you could use from pizza import make_pizza to specify a single function

# You can also give an alias to a function
# Example below:
# from pizza import make_pizza as mp

# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# from module_name import function_name as fn