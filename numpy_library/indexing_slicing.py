import numpy as np

# indexing and slicing of array
"""
indexing - numpy arrays are zero indexed. It follows positive indexing (0, 1, 2, ...) and negative indexing (-1, -2, -3, ...).

slicing - accessing a range of elements in an array. It follows the syntax arr[start:stop:step] where start is the index of the first element to include, stop is the index of the first element to exclude, and step is the number of indices to skip.

step = 1 (default) means no skipping, step = 2 means skip one element, step = 3 means skip two elements and so on.

step = -1 means reverse the array.
"""
arr = np.array([1,2,3,4,5])

print(arr[0]) # prints 1
print(arr[-1]) # prints 5

print(arr[1:3]) # prints [2 3] (slices the array from index 1 to index 2)

print(arr[1:]) # prints [2 3 4 5] (slices the array from index 1 to the end of the array)

print(arr[:3]) # prints [1 2 3] (slices the array from the beginning to index 2)

print(arr[::2]) # prints [1 3 5] (slices the array from the beginning to the end of the array with a step of 2)

print(arr[::-1]) #! prints [5 4 3 2 1] (reverses the array)

"""
when step is negative, the default start and stop values change.
Default start becomes the last element
Default stop becomes before the first element (conceptually index -1)
"""