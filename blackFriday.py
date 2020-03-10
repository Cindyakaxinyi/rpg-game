# Cindy Li
# Feb 25, 2020
# CS30
# Janice Cotcher
# Black Friday shopping simulator at Target's appliances section

# game characters
characters = ["Target employee", "Karen", "security", "crowd"]
# appliances at Target
items = ["Samsung smart TV", "LG minifridge", "Marble top microwave",
         "Gold plated toddler walker", "Rice cooker"]
# prints characters
print(f"Obstacles in the game: {characters}")

# prints appliances
print(" ")
print(f"Appliances at target: {items}")

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

# append() command
characters.append("Cashier")
print(" ")
print("The final character you need to face is the " + str(characters[4]))

# insert() command
items.insert(5, "Ornament string lights for decoration, warm white")
print(" ")
print("you will have an option to steal an additional item if you have enough")
print("points: " + str(items[5]))

# del() command
del items[5]
print(" ")
print("if you dont have enough, you will be confined to buying these items")
print(items)

# pop() command
v = characters.pop()
print(" ")
print(f"if you don't steal, the {v} won't be suspicious")

# remove() command
expensive = "Gold plated toddler walker"
items.remove(expensive)
print(" ")
print(f"you could run out of money, and the {expensive} will be unaffordable")
print(f"you will be confined to buying these items: {items}")
