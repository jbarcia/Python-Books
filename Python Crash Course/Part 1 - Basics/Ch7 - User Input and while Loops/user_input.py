#! /usr/bin/python
# If you’re using Python 2.7, you should use the raw_input() function when prompting for user input. 
# This function interprets all input as a string

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

print()
# Writing Clear Prompts
name = input("Please enter your name: ")
print("Hello, " + name + "!")

print()
# Multiline prompt
prompt = "If you tell us who you are, we can personalize the messages you see."
# operator += takes the string that was stored in prompt and adds the new string onto the end.
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

print()
# Using int() to Accept Numerical Input
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

print()
# The Modulo Operator
# The modulo operator doesn’t tell you how many times one number fits into another; it just tells you what the remainder is.
# When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0.
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")


