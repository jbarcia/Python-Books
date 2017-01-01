#! /usr/bin/python
# tuples - a list of items that cannot change
# When compared with lists, tuples are simple data structures. 
# Use them when you want to store a set of values that should not be changed throughout the life of a program.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print()
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
