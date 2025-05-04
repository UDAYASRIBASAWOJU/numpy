import numpy as np

arr = np.array([2, 5, np.nan, 4, np.nan, 7, np.nan])
print(arr)

print(np.nan_to_num(arr))
print(np.nan_to_num(arr, nan=3))
