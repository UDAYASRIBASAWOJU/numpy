import numpy as np

arr = np.array([[1,3,4],[5,7,8]])
print(arr)
new_arr = np.insert(arr, 2, [2,3,6], axis=0)
print(new_arr)
new_arr1 = np.insert(arr, 1, [2,3], axis=1)
print(new_arr1)
