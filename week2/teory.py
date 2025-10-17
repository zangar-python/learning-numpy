import numpy as np
# indexing

arr = np.arange(10)
indeces = [1,4,7]
print(arr[indeces])


print(np.take(arr,[1,2,3]))
np.put(arr,[1,2,3],[100,200,3000])
dio = arr[:3]-100

random_arr = np.random.randint(dio[0],dio[-1],100)
# random_arr[random_arr<0] = 0
print(np.where(random_arr<0))
blocked_users = np.where(random_arr<0)
np.put(random_arr,blocked_users,0)
print(random_arr)
