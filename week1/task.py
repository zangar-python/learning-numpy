import numpy as np

arr = np.random.randn(1000)

print(arr.max())
print(arr.min())
print(arr.mean())

print(len((arr[arr > 1])))