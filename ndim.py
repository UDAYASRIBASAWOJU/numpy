import numpy as np

arr_1d = np.array([3,5,6])
arr_2d = np.array([[3,5,6], [2,4,7]])
multi_d = np.array([[[3,5,6], [2,4,7], [3,4,5], [5,7,9], [3,4,5]]])

print(arr_1d.ndim)
print(arr_2d.ndim)
print(multi_d.ndim)
