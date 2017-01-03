#! /usr/bin/python

# Defining a Function
def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

# Passing Information to a Function
def greet_user2(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greet_user2('jesse')
