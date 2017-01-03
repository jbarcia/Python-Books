#! /usr/bin/python
# storing your functions in a separate file called a module and then importing that module into your main program. 
# An import statement tells Python to make the code in a module available in the currently running program file.

# Importing an Entire Module
import pizza
# If you use this kind of import statement to import an entire module named module_name.py, each function in the module is
# available through the following syntax: module_name.function_name()
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


print()
# Importing Specific Functions
# You can also import a specific function from a module. Here’s the general syntax for this approach:
# 		from module_name import function_name
# You can import as many functions as you want from a module by separating each function’s name with a comma:
# 		from module_name import function_0, function_1, function_2
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


print()
# Using as to Give a Function an Alias
# If the name of a function you’re importing might conflict with an existing 
# name in your program or if the function name is long, you can use a short, unique alias
# The general syntax for providing an alias is:
# 		from module_name import function_name as fn
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


print()
# Using as to Give a Module an Alias
# You can also provide an alias for a module name. Giving a module a short alias, 
# like p for pizza, allows you to call the module’s functions more quickly.
# readability of your code than using the full moThe general syntax for this approach is:
# 		import module_name as mn
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


print()
# Importing All Functions in a Module
# You can tell Python to import every function in a module by using the asterisk (*) operator:
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


