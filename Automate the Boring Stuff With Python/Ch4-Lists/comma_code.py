# Comma Code

# Defined lists
Sizes = ['small', 'medium', 'large', 'extra-large']
Colors = ['red', 'blue', 'green']
Prices = ['100 USD', '200USD']
One_item = ['hi']
Empty = []


def enumerate(list_name):  # Function takes in a list
    # Print only items before the last item
    if len(list_name) > 2:
        for item in list_name[:-1]:
            print(item, ', ', sep='', end='')
        print('and ', end='')
        print(list_name[-1])
    elif len(list_name) == 2:
        print(list_name[0], 'and', list_name[1])
    elif len(list_name) == 1:
        print(list_name[0])
    else:
        print('There are no items in this list.')


# Replace list with any list you want
# Possible lists to pass in: Sizes, Colors, Prices, One_Item, and Empty
enumerate(Empty)
