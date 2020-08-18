'''
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1.
'''

array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 2, 1, 2]
length = len(array1)


def function(array1, array2):
    return [array1[x] * array2[x] for x in range(0, length)]


print(function(array1, array2))
