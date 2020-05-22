# Vasallius

""" This program displays total price after making your custom sandwhich"""


import pyinputplus as pyip  # Import necessary modules

# Initialize variables
breadtypes = ['White', 'Wheat', 'Sourdough']
proteintypes = ["chicken", "turkey", "ham", "tofu"]
cheesetypes = ["cheddar", "Swiss", "mozzarella"]

pricelist = {"White": 20, "Wheat": 15, "Sourdough": 25,
             "chicken": 25, "turkey": 15, "ham": 20, "tofu": 10,
             "cheddar": 10, "Swiss": 12, "mozzarella": 14}

totalcost = 0

# Functions that ask for user input and store them in a variable
# Add price to variable totalcost
bT = pyip.inputMenu(breadtypes,
                    prompt=f'''What type of bread would you like ?
* {breadtypes[0]} 
* {breadtypes[1]} 
* {breadtypes[2]} \n''')

totalcost += pricelist[bT]

pT = pyip.inputMenu(proteintypes,
                    prompt=f'''What type of protein would you like ?
* {proteintypes[0]} 
* {proteintypes[1]} 
* {proteintypes[2]}
* {proteintypes[3]} \n''')

totalcost += pricelist[pT]

cT = pyip.inputMenu(cheesetypes,
                    prompt=f'''What type of cheese would you like ?
* {cheesetypes[0]} 
* {cheesetypes[1]} 
* {cheesetypes[2]} \n''')

totalcost += pricelist[cT]

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

# Print total cost
print(f"\nThank you for ordering. That would be {totalcost} $")
