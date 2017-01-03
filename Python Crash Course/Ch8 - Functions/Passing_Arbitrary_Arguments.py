#! /usr/bin/python

# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print()
	print(toppings)
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print()
# Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the parameter that accepts 
# an arbitrary number of arguments must be placed last in the function definition. 
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) +
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print()
# Using Arbitrary Keyword Arguments
# Sometimes you’ll want to accept an arbitrary number of arguments, but you
# won’t know ahead of time what kind of information will be passed to the function
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')
print(user_profile)

