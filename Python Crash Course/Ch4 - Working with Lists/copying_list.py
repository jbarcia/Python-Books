#! /usr/bin/python

my_foods = ['pizza', 'falafel', 'carrot cake']
# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ( [:]). 
# This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
friend_foods = my_foods[:]

# Add food to my list
my_foods.append('cannoli')
# Add food to friend list
friend_foods.append('ice cream')

# Print lists
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


# This syntax actually tells Python to connect the new variable friend_foods to the list that is already contained in
# my_foods, so now both variables point to the same list. 
friend_foods = my_foods
# Add food to my list
my_foods.append('apple pie')
# Add food to friend list
friend_foods.append('custard pie')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
