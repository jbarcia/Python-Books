#! /usr/bin/python

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# Conditional Tests
print()
# Ignoring Case When Checking for Equality
car = 'Audi'
print(car)
print(car.lower() == 'audi')

print()
# Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

print()
# Numerical Comparisons
answer = 17
print("The answer is: " + str(answer))
if answer != 42:
	print("That is not the correct answer. Please try again!")
if answer == 17:
	print("The answer is 17!")
if answer < 21:
	print("The answer is less than 21!")
if answer <= 21:
	print("The answer is less than or equal to 21!")
if answer > 21:
	print("The answer is greater than 21!")
if answer >= 21:
	print("The answer is greater than or equal to 21!")

# Checking Multiple Conditions
print()
# Using and to Check Multiple Conditions
age_0 = 22
age_1 = 18
print("age_0 = " + str(age_0))
print("age_1 = " + str(age_1))
if age_0 >= 21 and age_1 >= 21:
	print("age_0 >= 21 and age_1 >= 21")
# OPTIONAL: To improve readability, you can use parentheses around the individual tests
if (age_0 >= 21) and (age_1 <= 21):
	print("age_0 >= 21 and age_1 <= 21")
# Using or to Check Multiple Conditions
if age_0 >= 20 or age_1 >= 21:
	print("age_0 >= 20 or age_1 >= 21")
# OPTIONAL: To improve readability, you can use parentheses around the individual tests
if (age_0 >= 20) or (age_1 <= 21):
	print("age_0 >= 20 or age_1 <= 21")

print()
# Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
	print("mushrooms is included")
if 'pepperoni' in requested_toppings:
	print("pepperoni is included")

print()
# Checking Whether a Value Is not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

print()
# Boolean Expressions
game_active = True
can_edit = False
if game_active:
	print("game_active")
if can_edit:
	print("can_edit")


