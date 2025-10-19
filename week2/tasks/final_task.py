import numpy as np

coordinates = np.random.randint(1,100,size=(1000,2))
center = np.random.randint(1,100,size=2)


normal_coor = (coordinates - coordinates.min(axis=0)) / (coordinates.max(axis=0) - coordinates.min(axis=0))

normal_center = (center - center.min(axis=0)) / (center.max(axis=0) - center.min(axis=0))

distance = np.sqrt(np.sum( (normal_coor - normal_center)**2,axis=1 ))

print(center)
print(np.sum(coordinates[distance < 0.2],axis=1))