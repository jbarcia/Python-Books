#! /usr/bin/python

# Moving Items from One List to Another

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

print()
# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

print()
# Filling a Dictionary with User Input
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	# Store the response in the dictionary:
	responses[name] = response
	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")

