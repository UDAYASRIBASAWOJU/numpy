import numpy as np

array = np.array([[3,5.3,6], [2,4,7]])

print(array)
print(array.dtype)
print('')

float = array.astype(float)
print(float)
print(float.dtype)
print('')

int = array.astype(int)
print(int)
print(int.dtype)
