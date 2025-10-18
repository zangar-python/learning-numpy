import numpy as np 
import time
m = 3
n = 4


arr1 = np.random.randint(1,10,size=(m,n))
batch = np.random.randint(1,10,size=n)

# 1
# print(arr1@arr2)

# 2
# print(arr1.dot(arr2))
# arr3 =  np.array([
#     [1,2,3],
#     [4,5,6]
# ]
# )
arr3 = np.dot(arr1,batch)
# arr4 = arr1*batch

print(arr3)
# print(arr4)

# arr3 = arr3.T

# print(arr3)

start = time.time()
matrix1 = np.random.randint(10,1000,size=(10,1000000))
matrix2 = np.random.randint(10,1000,size=(10,1000000))

matrix3 = matrix1*matrix2
print(matrix3)
print(time.time()-start)