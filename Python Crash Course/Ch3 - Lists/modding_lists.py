
# modifying lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# replacing at the begining (location 0) 
motorcycles[0] = 'ducati'
print(motorcycles)

# Appending at the end of the list
motorcycles.append('honda')
print(motorcycles)


print()
# Creating a new list and appending new items
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)


print()
# Inserting into a list location 0
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)


print()
# Removing from a list using del
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)


print()
# Removing from a list using pop
# pop() method removes the last item in a list, but it lets you work
# with that item after removing it. 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print()
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")


print()
# Removing from a list using pop from any location
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")


print()
# Removing from a list by value
# The remove() method deletes only the first occurrence of the value you specify. If a possibility the value appears more than once in the list, you’ll need to use a loop
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

