#! /usr/bin/python

# Python can only write strings to a text file. If you want to store numerical data in a
# text file, you’ll have to convert the data to string format first using the str() function.

# Writing to an Empty File
filename = 'programming.txt'
with open(filename, 'w') as file_object:
	# Writing Multiple Lines
	file_object.write("I love programming.")
	file_object.write("I love creating new games.")
	# newlines
	file_object.write("\nI love programming.\n")
	file_object.write("I love creating new games.\n")

# Appending to a File
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")

