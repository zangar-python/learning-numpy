import numpy as np
coordinates_obj = np.random.randint(1,1000,size=(10,3))
center = np.array([500,500,500])

distance =np.sqrt(np.sum((coordinates_obj - center) ** 2,axis=1))
print(coordinates_obj[distance < 200])