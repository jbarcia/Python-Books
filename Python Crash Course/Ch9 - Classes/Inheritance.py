#! /usr/bin/python

# You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized version of another class you wrote, you can
# use inheritance. When one class inherits from another, it automatically takes on all the attributes and methods of the first class. The original class is
# called the parent class, and the new class is the child class. The child class inherits every attribute and method from its parent class but is also free to
# define new attributes and methods of its own.

# Inheritance in Python 2.7
# class Car(object):
# 	def __init__(self, make, model, year):
# class ElectricCar(Car):
# 	def __init__(self, make, model, year):
# 		super(ElectricCar, self).__init__(make, model, year)

class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles

# Instances as Attributes
class Battery():
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)


class ElectricCar(Car):
	"""
	Initialize attributes of the parent class.
	Then initialize attributes specific to an electric car.
	"""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		self.battery = Battery()
		self.battery_size = 70
	# Defining Attributes and Methods for the Child Class
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	# Overriding Methods from the Parent Class
	def fill_gas_tank():
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
print()
# Defining Attributes and Methods for the Child Class
my_tesla.describe_battery()
print()
# Instances as Attributes
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
