#! /usr/bin/python
# Changing Case in a String with Methods
name = "ada lovelace"

# Ada Lovelace
print(name.title())
# ADA LOVELACE
print(name.upper())
# ada lovelace
print(name.lower())

print()
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)


# add a tab to your text

print("Python")
print("\tPython") 

# add a newline in a string
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript") 

print()
# Stripping Whitespace
favorite_language = ' python '

# right strip - ' python' 
print(favorite_language.rstrip())

# left strip - 'python '
print(favorite_language.lstrip())

# strip both - 'python'
print(favorite_language.strip())



print()
# Using integers in strings
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)