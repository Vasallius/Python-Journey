'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''


def sum_of_squares_of_odd_positive_integers(n):
    odd_positive = [x for x in range(1, n, 2)]
    return sum(x ** 2 for x in odd_positive)


print(sum_of_squares_of_odd_positive_integers(5))
