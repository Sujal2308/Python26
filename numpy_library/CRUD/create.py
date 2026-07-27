
import numpy as np

#! creating array if we have a pre-defined list of items
arr = np.array([1, 2, 3, 4, 5])

#! create an array of zeros
arr_zeros = np.zeros((2, 3)) # creates a 2x3    
arr_zeros_1d = np.zeros(5) # creates a 1D array of 5 zeros

print(arr)
print(arr_zeros)
print(arr_zeros_1d)

'''
Note : By default numpy creates an array of float data type.
But we can specify the data type of the array using dtype parameter.
'''

new_arr = np.ones(5,dtype=int) # creates a 1D array of 5 ones of int data type
print(new_arr)

'''
empty array - creates an array without initializing the values. The values will be random and depend on the state of the memory.
'''

arr_empty = np.empty((2, 3)) # creates a 2x3 empty array
print(arr_empty)

arr_empty_1d = np.empty(5) # creates a 1D empty array of 5 elements
print(arr_empty_1d)