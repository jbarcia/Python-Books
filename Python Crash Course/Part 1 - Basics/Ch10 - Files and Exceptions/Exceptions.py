#! /usr/bin/python

'''
Exceptions are handled with try-except blocks. A try- except block asks
Python to do something, but it also tells Python what to do if an excep-
tion is raised. When you use try-except blocks, your programs will continue
running even if things start to go wrong. Instead of tracebacks, which can
be confusing for users to read, users will see friendly error messages that
you write.
'''

# Using try-except Blocks
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

# Using Exceptions to Prevent Crashes
print()
# The else Block
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)

print()
# Handling the FileNotFoundError Exception
filename = 'alice.txt'
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
		print(contents)
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
# Analyzing Text
else:
	# Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")

print()
# Working with Multiple Files
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		# Count approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

# Failing Silently
try:
	print(5/0)
except ZeroDivisionError:
	# Failing Silently
	pass
