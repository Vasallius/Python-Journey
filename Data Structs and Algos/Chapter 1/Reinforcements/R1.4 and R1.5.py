'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''


def sum_of_squares(n):
    positive = [x for x in range(1, n)]
    return sum(x ** 2 for x in positive)


print(sum_of_squares(5))
