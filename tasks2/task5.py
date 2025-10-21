import numpy as np

points = np.random.rand(10_000,2)
center = np.array([0.5,0.5])

coordinates = np.sqrt(np.sum((points - center)**2,axis=1))

print(len(points[coordinates <= 0.1,:])/(len(coordinates)/100))

print(np.mean(points,axis=1).mean())