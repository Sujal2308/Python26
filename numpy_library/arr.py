import numpy as np

arr_1d = np.array([1,2,3,4,5])
print(arr_1d)

#size of array -returns the total number of elements in the array
print(arr_1d.size)

# shape of array - returns no of rows and columns in the array
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.shape)

# dimension of array - returns the number of dimensions of the array
print(arr_2d.ndim)
print(arr_1d.ndim)

# Note : for 2d array size is equal to the product of rows and columns
print(arr_2d.size)

# data type of array - returns the data type of the array
print(arr_1d.dtype) # int64 because all elements are integers
temp_arr = np.array([1,2,3,4.5,6])
print(temp_arr.dtype) #float64 because of 4.5

# Converting data type of array - we can convert the data type of array using astype() method

float_arr = np.array([1.2,2.3,3.4,4.5,5.6])
int_arr = float_arr.astype(int)
print(float_arr) # float64
print(int_arr) # int64 [1 2 3 4 5]


# element wise operations on array - we can perform element wise operations on array using arithmetic operators
arr_1 = np.array([1,2,3,4,5])
print(arr_1 + 2) # adds 2 to each element of the array
print(arr_1 * 2) # multiplies each element of the array by 2

"""
aggregate functions on array - we can perform aggregate functions on array using numpy methods

Note: aggregate functions are functions that summarize the data in some way. They take an array as input and return a single value as output. Some common aggregate functions are sum, mean, std, min, max, median, var etc.

"""

print(np.sum(arr_1)) # returns the sum of all elements in the array
print(np.mean(arr_1)) # returns the mean of all elements in the array
print(np.std(arr_1)) # returns the standard deviation of all elements in the array
print(np.min(arr_1)) # returns the minimum element in the array
print(np.max(arr_1)) # returns the maximum element in the array
print(np.median(arr_1)) # returns the median of all elements in the array
print(np.var(arr_1)) # returns the variance of all elements in the array




