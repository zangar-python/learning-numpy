import numpy as np

arr1 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

for arrs in arr1:
    arrs += 5
    print(arrs)

