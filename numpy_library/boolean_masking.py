"""
boolean masking aka filtering : accessing elements of an array based on a boolean condition
"""

import numpy as np

arr = np.array([10, 21, 30, 40, 55])

print(arr[arr>30]) # prints [40 55] (selects elements greater than 30)

print(arr[arr%2==0]) # prints [10 30 40] (selects even elements)