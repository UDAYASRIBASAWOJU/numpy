import numpy as np

arr = np.array([2, 5, np.inf, 4, np.inf, 7, -np.inf])
print(arr)
print(np.isinf(arr))
print(np.nan_to_num(arr, posinf = 10, neginf = -10))
