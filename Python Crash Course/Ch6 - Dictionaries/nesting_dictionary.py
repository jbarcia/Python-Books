#! /usr/bin/python
# Sometimes you’ll want to store a set of dictionaries in a list or a list of
# items as a value in a dictionary. This is called nesting. You can nest a set
# of dictionaries inside a list, a list of items inside a dictionary, or even a
# dictionary inside another dictionary.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

# use range() to create a fleet of 30 aliens
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(0,30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# modify the first three aliens, modifying green and yellow aliens
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

# Show the first 5 aliens:
for alien in aliens[:5]:
	print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

print()
# A List in a Dictionary
# Store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)

print()
# Nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary.
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())

print()
# A Dictionary in a Dictionary
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
