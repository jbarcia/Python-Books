#! /usr/bin/python

# Returning a Simple Value
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print()
# Making an Argument Optional
def get_formatted_name2(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name2('john', 'lee', 'hooker')
print(musician)
musician = get_formatted_name2('jimi', 'hendrix')
print(musician)

print()
# Returning a Dictionary
def build_person(first_name, last_name, age=''):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print()
#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")
