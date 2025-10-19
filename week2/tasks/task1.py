import numpy as np
import time 

arr = np.random.randint(1,100,size=(10,10))
sorted_arr = np.sort(arr)
# print(sorted_arr)
idx = np.argsort(arr)
# print(idx)
new_arr = sorted_arr[sorted_arr<20]
# print(new_arr)
# print(arr)
norm_arr = (arr - arr.min())/(arr.max()-arr.min())
# print(norm_arr)

points = np.random.rand(100,2)
center = np.array([0.5,0.5])

distances = np.sqrt(np.sum((points - center) ** 2,axis=1))

mean_dist = distances.mean()
cluster1 = points[points <= mean_dist]
cluster2 = points[points > mean_dist]

print("cluster 1 :",cluster1.shape)
print("cluster 2 :",cluster2.shape)
print(distances)