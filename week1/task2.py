import numpy as np

matrix = np.random.randint(-100,100,size=(10,10))
matrix[matrix<0] = 0

harizontal_sum_1 = matrix[1,:].sum()

vertikal_sum_1 = matrix[:,1].sum()

broad_casting = np.arange(10)


print(matrix)
print(harizontal_sum_1)
print(vertikal_sum_1)
new_arr = broad_casting + matrix
print(new_arr)
print(new_arr-broad_casting)
