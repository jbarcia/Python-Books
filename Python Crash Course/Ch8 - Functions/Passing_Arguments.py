#! /usr/bin/python

# Positional Arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
# Multiple Function Calls
describe_pet('dog', 'willie')

# Keyword Arguments
# keyword argument is a name-value pair that you pass to a function
# When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition.
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')

# Default Values
# When writing a function, you can define a default value for each parameter.
def describe_pet2(pet_name, animal_type='dog'):
	# When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. 
	# This allows Python to continue interpreting positional arguments correctly.

	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet2(pet_name='willie')
describe_pet2(pet_name='harry', animal_type='hamster')


print()
# Equivalent Function Calls

# A dog named Willie.
describe_pet2('willie')
describe_pet2(pet_name='willie')
# A hamster named Harry.
describe_pet2('harry', 'hamster')
describe_pet2(pet_name='harry', animal_type='hamster')
describe_pet2(animal_type='hamster', pet_name='harry')
