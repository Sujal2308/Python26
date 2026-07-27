"""
reshape : changing the shape of an array without changing its data  
Think of it like rearranging books on a shelf:
Same books ✅
Different arrangement ✅

Note : The total number of elements must remain the same.
formula = rows × columns = total elements

Note : reshaping an array does not change the original array. It returns a new array with the new shape.
"""

import numpy as np

arr = np.array([1, 2, 3,4,5,6]) # total elements = 6
print(arr.reshape(2, 3)) # valid reshape because 2 × 3 = 6
print(arr.reshape(3, 2)) # valid reshape because 3 × 2 = 6
print(arr.reshape(6, 1)) # valid reshape because 6 × 1 = 6

#print(arr.reshape(2,2)) # invalid reshape because 2 × 2 = 4 which is not equal to 6

arr_2d = arr.reshape(2, 3)

print(arr_2d)
print(arr)