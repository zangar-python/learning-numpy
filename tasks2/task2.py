import numpy as np

active = np.random.randint(1,100,size=(100,7))

mean_week_day = np.mean(active,axis=0)

mean_day = np.mean(active,axis=1)

all_mean = mean_day.mean()
super_activity = active.mean(axis=1) > all_mean

print(active[super_activity,:])
print(mean_week_day)
