#! /usr/bin/python
# In Python 2.7 => class ClassName(object):

# Create a function. Functions do specific things, classes are specific things.
# Classes often have methods, which are functions that are associated with a particular class, 
# and do things associated with the thing that the class is - but if all you want is to do something, 
# a function is all you need. Essentially, a class is a way of grouping functions (as methods) and data (as properties) 
# into a logical unit revolving around a certain kind of thing. If you don't need that grouping, there's no need to make a class.

class Dog():
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

# Accessing Attributes
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Calling Methods
my_dog.sit()
my_dog.roll_over()

print()
# Creating Multiple Instances
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
