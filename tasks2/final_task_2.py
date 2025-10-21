import numpy as np

users = np.random.randint(0,2,size=(100,20))
user = np.random.randint(0,2,size=20)

norm_users = np.linalg.norm(users,axis=1)
norm_user = np.linalg.norm(user)

coef = (users@user) / (norm_users * norm_user)

top_5_users = np.argsort(coef)[::-1][:5]

max_coef = np.max(coef)
print(f"Top 5 users :",users[top_5_users],sep="\n")
# print(max_coef)
print(f"User :",user)
print("Users like him :\n",users[max_coef == coef])