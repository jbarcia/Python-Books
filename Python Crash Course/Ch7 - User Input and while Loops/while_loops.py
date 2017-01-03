#! /usr/bin/python

# while loop counts from 1 to 5
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

print()
# Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)

print()
# Using a Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)

print()
# Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
	# A loop that starts with while True u will run forever unless it reaches a break statement. 
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")

print()
# Using continue in a Loop
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		#  the continue statement tells Python to ignore the rest of the loop and return to the beginning
		continue
	print(current_number)
