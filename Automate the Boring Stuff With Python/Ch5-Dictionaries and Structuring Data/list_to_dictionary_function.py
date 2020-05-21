#© Vasallius

def display_inventory(inventoryname):
    totalitems= 0
    for k,v in inventoryname.items():
        print (v,k)
        totalitems += v
    print('Total number of items: ' + str(totalitems) )

def addToInventory(inventory, addedItems):
    for item in dragonLoot:
        inventory[item] = inventory.get(item,0)+1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print('Inventory:')
inv = addToInventory(inv, dragonLoot)
display_inventory(inv)
