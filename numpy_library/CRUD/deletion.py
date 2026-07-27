"""
delete(array, indices, axis=None) : deletes elements from an array along a specified axis. It returns a new array with the specified elements removed.
Note : The original array is not modified. It returns a new array with the specified elements removed
"""
import numpy as np
arr = np.array([1, 2, 3,4,5,6])
print(np.delete(arr, 2)) # deletes the element at index 2 and returns a new array [1 2 4 5 6]

# removing multiple elements at once
print(np.delete(arr, [1, 3])) # deletes the elements at indices 1 and 3 and returns a new array [1 3 5 6]

# deleting from a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(np.delete(arr_2d, 1, axis=0)) # deletes the row at index 1 and returns a new array [[1 2 3]]
print(np.delete(arr_2d, 1, axis=1)) # deletes the column at index 1 and returns a new array [[1 3] [4 6]]