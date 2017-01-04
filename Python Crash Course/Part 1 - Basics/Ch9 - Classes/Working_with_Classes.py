#! /usr/bin/python

class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		# Setting a Default Value for an Attribute
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	# Modifying an Attribute’s Value Through a Method
	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	# Incrementing an Attribute’s Value Through a Method
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print("You can't roll back an odometer!")
		
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print()
# Modifying an Attribute’s Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print()
# Modifying an Attribute’s Value Through a Method
my_new_car.update_odometer(26)
my_new_car.read_odometer()

print()
# Incrementing an Attribute’s Value Through a Method
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
