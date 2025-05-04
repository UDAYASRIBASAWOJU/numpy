import numpy as np

arr1 = np.array([1,3,4])
arr2 = np.array([5,7,8])
new_arr1=np.vstack((arr1, arr2))
print(new_arr1)
new_arr2=np.hstack((arr1, arr2))
print(new_arr2)
