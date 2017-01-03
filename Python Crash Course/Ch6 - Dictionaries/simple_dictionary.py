#! /usr/bin/python
# A dictionary in Python is a collection of key-value pairs. Each key is connected
# to a value, and you can use a key to access the value associated with that key.
# In Python, a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces

# A Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
# Accessing Values in a Dictionary
print(alien_0)
print(alien_0['color'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print()
# Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print()
# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print()
# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

print()
# Track the position of an alien that can move at different speeds
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


print()
# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

print()
# A Dictionary of Similar Objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print("Sarah's favorite language is " +
	favorite_languages['sarah'].title() +
	".")
