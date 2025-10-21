import numpy as np

points = np.random.rand(100,3)

A_center = np.array([0.3,0.3,0.3])
B_center = np.array([0.7,0.7,0.7])

A_coor = np.sqrt( np.sum( (points - A_center)**2,axis=1 ) )
B_coor = np.sqrt( np.sum( (points - B_center)**2,axis=1 ) )

claster_A = points[A_coor <= 0.2]
claster_B = points[B_coor <= 0.2]

print(claster_A)
print(claster_B)