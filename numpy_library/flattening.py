"""
flattening means converting a multi-dimensional array into a one-dimensional array. In numpy, we can flatten an array using the flatten() method or the ravel() method.

ravel() - mutates the original array
flatten() - does not mutate the original array rather returns a new array that is a flattened version of the original array.

"""

import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d.flatten()) # prints [1 2 3 4 5 6] (flattens the array into a one-dimensional array)
print(arr_2d.ravel()) # prints [1 2 3 4