#! /usr/bin/python

# A list usually contains more than one element, it’s a good idea to make the
# name of your list plural, such as letters, digits, or names.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#  first bicycle in the list bicycles:
print(bicycles[0])

# Use string methods
print(bicycles[0].title())

# Access the 2nd and 4th item
print(bicycles[1])
print(bicycles[3])

# Returns the last item in the list
print(bicycles[-1])

# Returns the second to last item in the list
print(bicycles[-2])

# Using Individual Values from a List
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

num = len(bicycles)
print("\n\nThere are " + str(num) + " bicycles in the list.")