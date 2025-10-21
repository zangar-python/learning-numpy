import numpy as np

arr = np.random.randint(1,1000,size=(100,2))

center = np.array([500,500])

print(arr)

mask_0 = arr[(center[0] < 20)&(center[0] > -20)]
mask_1 = arr[(center[1] < 20)&(center[1] > -20)]




# arr[arr[mask_0==False,0] > center[0],0] -= 20
# arr[arr[mask_0==False,0] < center[0]] += 20


# arr[arr[mask_1==False,1] > center[1]] -=20
# arr[[mask_1==False,1] < center[1]] +=20

print(mask_0)
print(mask_1)