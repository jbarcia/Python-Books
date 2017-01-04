#! /usr/bin/python
import json

# Using json.dump() and json.load()
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
# uses json.dump() to store a list of numbers
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)

# uses json.load() to read the list back into memory
with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)

print()
# Saving and Reading User-Generated Data
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
	json.dump(username, f_obj)
	print("We'll remember you when you come back, " + username + "!")

with open(filename) as f_obj:
	username = json.load(f_obj)
	print("Welcome back, " + username + "!")

print()
# Streamlining
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")
