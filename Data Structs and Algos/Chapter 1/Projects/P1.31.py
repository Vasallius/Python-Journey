'''
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
'''


def change(cost, payment):
    change = payment - cost
    one_hundred_bills, fifty_bills = divmod(change, 100)
    fifty_bills, twenty_bills = divmod(fifty_bills, 50)
    twenty_bills, ten_peso_coins = divmod(twenty_bills, 20)
    ten_peso_coins, five_peso_coins = divmod(ten_peso_coins, 10)
    five_peso_coins, one_peso_coins = divmod(five_peso_coins, 5)
    one_peso_coins, lol = divmod(one_peso_coins, 1)

    print('Change:', one_hundred_bills, fifty_bills, twenty_bills,
          ten_peso_coins, five_peso_coins, one_peso_coins)


change(100, 157)
