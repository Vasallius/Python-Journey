# Sandwich Maker

""" 
Description:
This program displays total price after making your custom sandwich.
"""

import pyinputplus as pyip

breadtypes = ['White', 'Wheat', 'Sourdough']
proteintypes = ["chicken", "turkey", "ham", "tofu"]
cheesetypes = ["cheddar", "Swiss", "mozzarella"]

pricelist = {"White": 20, "Wheat": 15, "Sourdough": 25,
             "chicken": 25, "turkey": 15, "ham": 20, "tofu": 10,
             "cheddar": 10, "Swiss": 12, "mozzarella": 14}

totalcost = 0

bread_type = pyip.inputMenu(breadtypes,
                            prompt='What type of bread would you like ? \n')
totalcost += pricelist[bread_type]

protein_type = pyip.inputMenu(proteintypes,
                              prompt=f'What type of protein would you like ? \n')
totalcost += pricelist[protein_type]

cheese_type = pyip.inputMenu(cheesetypes,
                             prompt=f'What type of cheese would you like ? \n')
totalcost += pricelist[cheese_type]

# Function that ask user for addons and increment totalcost by 5 per addon
mayo = pyip.inputYesNo(prompt="Do you want to add mayo?\n")
if mayo == 'yes':
    totalcost += 5
mustard = pyip.inputYesNo(prompt="Do you want to add mustard?\n")
if mustard == 'yes':
    totalcost += 5
lettuce = pyip.inputYesNo(prompt="Do you want to add lettuce?\n")
if lettuce == 'yes':
    totalcost += 5
tomato = pyip.inputYesNo(prompt="Do you want to add tomato?\n")
if tomato == 'yes':
    totalcost += 5

print(f"\nThank you for ordering. That would be {totalcost}$")
