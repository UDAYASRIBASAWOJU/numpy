import numpy as np

arr = np.array([1,3,4,5,7,8])
print(arr)
new_arr = np.insert(arr, 3, 2)
print(new_arr)
new_arr1 = np.insert(arr, 3, 2, axis=0)
print(new_arr1)
