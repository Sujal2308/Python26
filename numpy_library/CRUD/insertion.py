'''
Method to insert elements into a NumPy array.
append() : adds elements to the end of an array.
insert() : adds elements at a specified index in an array.

Note : Both methods return a new array and do not modify the original array.
'''
import numpy as np
#append() method
arr = np.array([1, 2, 3])
new_arr = np.append(arr, 4)
print(new_arr) # prints [1 2 3 4]

#? we can also append multiple elements at once np.append(arr, [4, 5, 6])


#insert() method
new_arr = np.insert(arr, 1, 5,axis=None) # inserts 5 at index 1
print(new_arr) # prints [1 5 2 3]

# insert in 2D array
arr_2d = np.array([[1, 2], [3, 4]])
new_arr_2d = np.insert(arr_2d, 1, 5, axis=0) # inserts 5 at index 1 along axis 0
print(new_arr_2d) # prints [[1 2] [5 5] [3 4]]

'''
axis defines the axis along which to insert the values.
axis=0 : insert along rows (vertical)
axis=1 : insert along columns (horizontal)  
axis=None : flattens the array and inserts the values at the specified index. It is the default value of axis.
'''

arr_2d  = np.array([[1,2,3],[4,5,6]])
print(np.insert(arr_2d, 1, [7,8,9])) # flattens the array and inserts [7,8,9] at index 1

print(np.insert(arr_2d, 1, [7,8,9], axis=0)) # inserts [7,8,9] at index 1 along axis 0

print(np.insert(arr_2d, 1, [7,8], axis=1)) # inserts [7,8] at index 1 along axis 1

#! Note : The shape of the values to be inserted must match the shape of the array along the specified axis. Otherwise, a ValueError will be raised.