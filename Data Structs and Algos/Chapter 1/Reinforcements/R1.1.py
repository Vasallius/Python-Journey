'''
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise
'''


def multiple(n, m):
    return True if m % n == 0 else False


print(multiple(10, 100))
