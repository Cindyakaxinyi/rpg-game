# Cindy Li
# Feb 24, 2020
# Black Friday shopping simulator at Target's appliances section

# game characters
characters = ["Target employee", "Karen", "security", "crowd"]
# appliances at Target
items = ["Samsung smart TV", "LG fridge", "Marble top microwave",
         "Gold plated toddler walker", "Rice cooker"]
# prints characters
print("Characters in the game:")
for character in characters:
    print(character)
# prints appliances
print(" ")
print("Appliances at target:")
for item in items:
    print (item)

# sorted() command
print(" ")
print("Appliances in alphabetical order:")
print(sorted(items))

# len() command
print(" ")
print("There are " + str(len(characters)) + " characters in this game")

# reverse() command
print(" ")
print("Characters in reversed order")
characters.reverse()
print(characters)

# sort() command
print(" ")
print("Characters in alphabetical order:")
characters.sort()
print(characters)
