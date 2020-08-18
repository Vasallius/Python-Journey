'''
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''


def minmax(data):
    biggest = data[0]
    smallest = data[0]
    for no in data:
        biggest = (no if no > biggest else biggest)
        smallest = (no if no < smallest else smallest)
    return smallest, biggest


print(minmax([1, 5, 189, 189, 82, 8, 81, 1, 2, 3, 4, 0]))
