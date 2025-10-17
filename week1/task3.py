import numpy as np

random_int = np.random.randint(1,1000,size=1000000)

print(random_int.mean())
print(random_int.max())
print(random_int.min())

levels = ["low","medium","high"]
conditions = [
    (random_int < 300),
    (random_int >= 300)&(random_int<700),
    random_int>=700
]
levels_arr = np.select(conditions,levels,default="any")

print(len(levels_arr[levels_arr=="low"]))
print(len(levels_arr[levels_arr=="medium"]))
print(len(levels_arr[levels_arr=="high"]))
