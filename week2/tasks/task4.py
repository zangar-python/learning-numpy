import numpy as np
arr1 = np.random.randint(1,10,size=(10,2))
arr2 = np.random.randint(1,10,size=(10,2))

d = np.sum(np.sqrt((arr1 - arr2) ** 2))

print(d)