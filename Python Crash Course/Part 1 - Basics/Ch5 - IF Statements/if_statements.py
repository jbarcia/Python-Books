#! /usr/bin/python

# Simple if statement
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
# if-else Statements
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

print()
# if-elif-else Chain
age = 12
print("Your age is " + str(age))
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

print()
# it would be more concise to set just the price inside the if-elif-else chain
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $" + str(price) + ".")

print()
# Using Multiple elif Blocks
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
print("Your admission cost is $" + str(price) + ".")

print()
# Omitting the else Block
# Python does not require an else block at the end of an if-elif chain. 
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5
print("Your admission cost is $" + str(price) + ".")
# The else block is a catchall statement. It matches any condition that wasn’t matched by a specific if or elif test, 
# and that can sometimes include invalid or even malicious data. 

print()
# Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")
# In summary, if you want only one block of code to run, use an if-elif-else chain. 
# If more than one block of code needs to run, use a series of independent if statements.
