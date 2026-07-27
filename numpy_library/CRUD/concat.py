'''
concatenates two or more arrays along a specified axis.
Note : The arrays must have the same shape along all axes except the one specified for concatenation

syntax : np.concatenate((arr1, arr2, ...), axis=0)
pass tuples of arrays to concatenate
'''

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
print(np.concatenate((arr1, arr2),axis=0)) # concatenates along axis

