# dictionary for appliances and their prices
# dictionary for characters and their weapons
# dictionary for locations of appliances

prices = {"Samsung smart TV": "1 099.99", "LG minifridge": "138.50",
          "Marble top microwave": "115.10", "Rice cooker": "149.69",
          "Gold plated toddler walker": "3 420.14"
          }

weapons = {"Security guard": {"tazer", "police stick", "pepper spray"},
           "Karen": "AIYUQI Loafers Genuine Leather Flat ladies shoes 2019",
           "Cashier": "portable cash register",
           "Target employee": "steel plated walkie talkie 2004",
           "crowd": "stampede"
           }

locations = {"Samsung smart TV": "shelf 1", "LG minifridge": "shelf 2",
             "Marble top microwave": "shelf 3", "Rice cooker": "shelf 4",
             "Gold plated toddler walker": "shelf 5"
             }

# prints out characters and their weapons
print("characters and their weapons")
for characters in weapons:
    weapon = weapons[characters]
    if characters == "Security guard":
        sw = weapons["Security guard"]
        print(f"the {characters}'s weapons are:")
        for w in sw:
            print(f"{w}")
    else:
        print(f"{characters}'s weapon is: {weapon}")

# prints out appliances and their prices
print("\n")
print("items you can store in your inventory")
print("prices in USD:")
print("\n")
for appliances in prices:
    p = prices[appliances]
    print(f"{appliances}: {p}")

# prints out location of items along Target's aisle 4
print("\n")
print("Location of items")
for item in locations:
    location = locations[item]
    print(f"{item} is on {location}")
