#! /usr/bin/python

# File Paths
# Linux / OSx
# OPTION1
# 	with open('text_files/filename.txt') as file_object:
# OPTION2
# 	file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# 	with open(file_path) as file_object:
# Windows
# OPTION1
# 	with open('text_files\filename.txt') as file_object:
# OPTION2
# 	file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
# 	with open(file_path) as file_object:

'''
When Python reads from a text file, it interprets all text in the file as a string. If you
read in a number and want to work with that value in a numerical context, you’ll
have to convert it to an integer using the int() function or convert it to a float using
the float() function.
'''

# Reading an Entire File
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
	print()
	#  remove the extra blank line during print
	print(contents.rstrip())

print()
# Reading Line by Line
filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		#print(line)
		#  remove the extra blank line during print
		print(line.rstrip())

print()
# Making a List of Lines from a File
# 	When you use with, the file object returned by open() is only available inside
# 	the with block that contains it. If you want to retain access to a file’s contents
# 	outside the with block, you can store the file’s lines in a list inside the block
filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())

print()
# Working with a File’s Contents
filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	# create a loop that adds each line of digits to pi_string and removes the newline character from each line
	pi_string += line.rstrip()

print(pi_string)
# print just the first 50 decimal places
print(pi_string[:52] + "...")
# print how long the string is
#  	The string is 32 characters long because it also includes the leading 3 and a decimal point
print(len(pi_string))

print()
# More manipulations
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
