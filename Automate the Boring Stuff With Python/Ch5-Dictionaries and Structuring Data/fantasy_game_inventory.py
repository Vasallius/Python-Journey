# credits: Vasallius


#initialize inventory dictionary
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventoryname):
    totalitems= 0
    for k,v in inventoryname.items():
        print (v,k)
        totalitems += v
    print('Total number of items: ' + str(totalitems) )

display_inventory(inventory)
