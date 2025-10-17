import numpy as np

arr = np.array([10,20,30,40,50,60])

index_1 = np.array([1,2,5])
index_2 = np.array([1,2,3,5])

mask = np.isin(index_2,index_1,invert=True)
only_2 = index_2[mask]

print(arr[index_1])
print(arr[index_2])
print(arr[only_2])