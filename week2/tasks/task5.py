import numpy as np

len_ = 10
arr1 = np.random.randint(1,100,size=len_)
arr2 = np.random.randint(1,100,size=len_)

def set_nomaliz(arr):
    len_ = len(arr)
    return np.sum(arr) / len_

arr1_normal = set_nomaliz(arr1)
arr2_normal = set_nomaliz(arr2)

up_fr = np.sum((arr1-arr1_normal)*(arr2-arr2_normal))

res = up_fr / (len_-1)
print(res)