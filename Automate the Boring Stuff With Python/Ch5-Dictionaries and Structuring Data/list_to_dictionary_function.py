# List to Dictionary Function

# Function taken from fantasy_game_inventory.py
def display_inventory(inventoryname):
    totalitems= 0
    for k,v in inventoryname.items():
        print (v,k)
        totalitems += v
    print('Total number of items: ' + str(totalitems))

# Takes in two dictionaries, first one being the inventory
# Second one being items to be added to the inventory
def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item,0)+1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print('Inventory:')
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
