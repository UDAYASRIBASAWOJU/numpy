import numpy as np

arr = np.array([1,3,4,5,7,8])
print((np.split(arr,3)))
print((np.hsplit(arr,2)))
arr1 = np.array([[1,3,4],[5,7,8]])
print((np.vsplit(arr1,2)))
