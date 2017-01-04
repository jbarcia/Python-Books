#! /usr/bin/python
# Note: Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase.

# Sorting a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

# Reverse Sort
cars.sort(reverse=True)
print(cars)

print()
# Temporary Sort
print("\nTemporary Sort:")
print(sorted(cars))
print("Here is the original list:")
print(cars)

print()
# Print List in Reverse Order
print(cars)
cars.reverse()
print(cars)

