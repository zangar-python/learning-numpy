import numpy as np

activity = np.random.randint(1,100,size=(1000,7))

normal_activity = (activity - activity.min())/(activity.max() - activity.min())


# top_mask = (normal_activity[:,0] > 0.5)& (normal_activity[:,1] > 0.5)&(normal_activity[:,2] > 0.5)&(normal_activity[:,3] > 0.5)&(normal_activity[:,4] > 0.5)&(normal_activity[:,5] > 0.5)&(normal_activity[:,6] > 0.5)
top_mask = np.all(normal_activity > 0.5,axis=1)


# mini_mask = (normal_activity[:,0] <= 0.5)& (normal_activity[:,1] <= 0.5)&(normal_activity[:,2] <= 0.5)&(normal_activity[:,3] <= 0.5)&(normal_activity[:,4] <= 0.5)&(normal_activity[:,5] <= 0.5)&(normal_activity[:,6] <= 0.5)
mini_mask = np.all(normal_activity<0.5,axis=1)

high_actvity_users = activity[top_mask].copy()
low_activity_users = activity[mini_mask].copy()


# print(high_actvity_users)
# print(low_activity_users)

mean_active = activity[np.any(normal_activity == 0.5,axis=1)]
# print(mean_active)

print(activity[np.all(normal_activity == 0.7,axis=1)])