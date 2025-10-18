import numpy as np

sales = np.random.randint(0,100,size=(30,5))

mean = np.mean(sales,axis=0)
median = np.median(sales,axis=0)
# median[median > 50]
# print(median)
# print(sales[sales>median])
# print(mean)
# print(median)
percent_high = (np.sum(sales>median, axis=0) / sales.shape[0]) * 100

res = np.array([
    mean,
    median,
    percent_high
])


for i in range(0,5):
    print(f"Product {i}: mean = {res[0,i]},median = {res[1,i]},percent = {res[2,i]}")
