import numpy as np

sales = np.random.randint(1,100,size=(100,5))

normaliz = (sales - sales.min()) / (sales.max() - sales.min())

coef = np.corrcoef(normaliz.T)

np.fill_diagonal(coef,0)
print(coef)
max_idx = np.unravel_index(np.argmax(coef),coef.shape)

print(max_idx[0],max_idx[1])