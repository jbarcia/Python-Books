#! /usr/bin/python

# range() function makes it easy to generate a series of numbers
for value in range(1,6):
	print(value)

print()
# Skip numbers in a given range
even_numbers = list(range(2,11,2))
print(even_numbers)
odd_numbers = list(range(1,11,2))
print(odd_numbers)

print()
# first 10 square numbers 
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)

print()
# first 10 square numbers alternative
squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)

print()
# Simple Statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

print()
# list comprehension allows you to generate list in just one line of code
squares = [value**2 for value in range(1,11)]
print(squares)

