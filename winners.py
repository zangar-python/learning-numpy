import numpy as np

user_with_scores = np.array([
    [1,90],
    [2,30],
    [3,67],
    [4,57],
    [5,35]
])
#print("scores:",user_with_scores[:,1])

winners = user_with_scores[:,1] > 50


print(user_with_scores[winners])
