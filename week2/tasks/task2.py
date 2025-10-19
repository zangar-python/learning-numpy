import numpy as np 

coordinates = np.random.rand(100_000,2)
center = np.random.rand(2)

distances = np.sqrt(np.sum((coordinates - center)**2,axis=1))

print(coordinates[distances < 0.2])