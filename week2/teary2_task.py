import numpy as np

sales = np.random.randint(1,100,size=1_000_000)

high_days = np.sum(sales > np.median(sales) )

print(high_days)

print(high_days/(len(sales)/100))
print(sales[sales > np.median(sales)])