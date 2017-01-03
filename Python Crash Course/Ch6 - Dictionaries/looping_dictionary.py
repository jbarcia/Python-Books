#! /usr/bin/python

# Looping Through All Key-Value Pairs
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

print()
# Looping Through All Key-Value Pairs - Example 2
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	language.title() + ".")

print()
# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
	print(name.title())
# Looping through the keys is actually the default behavior when looping through a dictionary
print("\nAlternative Output:")
for name in favorite_languages:
	print(name.title())

print()
# Loop through the names in the dictionary, but when the name matches one of our friends, we’ll
# display a message about their favorite language:
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print("   Hi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")

print()
# You can also use the keys() method to find out if a particular person was polled.
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

print()
# Looping Through a Dictionary’s Keys in Order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

print()
# Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

print()
# To see each language chosen without repetition, we can use a set.
# A set is similar to a list except that each item in the set must be unique:
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
