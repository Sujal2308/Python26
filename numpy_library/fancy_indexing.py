"""
fancy indexing - abilty to access multiple array elements at once using an array of indices. It allows you to select arbitrary elements from an array based on their indices.

"""

import numpy

arr = numpy.array([10, 20, 30, 40, 50])

print(arr[[0, 2, 4]]) # prints [10 30 50] (selects elements at indices 0, 2, and 4) 

print(arr[[1,1,2,3]]) # Repitition of indices is allowed. prints [20 20 30 40] (selects elements at indices 1, 1, 2, and 3)

print(arr[[4,3,0]]) # order agnostic 

