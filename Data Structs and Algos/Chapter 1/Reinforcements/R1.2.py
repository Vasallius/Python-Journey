'''
Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''


def is_even(k):
    while k > 2:
        k -= 2
    return bool(k-1)


print(is_even(0), is_even(1))
