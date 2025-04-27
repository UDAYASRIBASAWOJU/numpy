import numpy as np

array = np.array([[3,5.3,6], [2,4,7]])

print(array.dtype)

float = array.astype(float)
print(float)
print(float.dtype)

int = array.astype(int)
print(int)
print(int.dtype)
