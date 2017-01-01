#! /usr/bin/python

# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# first three players
print(players[0:3])
# players 3 - 5
print(players[2:5])
# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:
print(players[:4])
# third item through the last item
print(players[2:])
# output the last three players
print(players[-3:])

print()
# looping through a list
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

