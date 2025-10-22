import numpy as np

users_id = np.arange(1,100)
users_likes = np.random.randint(0,2,size=(len(users_id),5))

user_likes = np.array([0,0,0,1,1])

norm_users = np.linalg.norm(users_likes,axis=1)
norm_user = np.linalg.norm(user_likes)

eps = 1e-10 
coef = (users_likes@user_likes)/(norm_users*norm_user+eps)

max_coef = np.max(coef)
# users_id = users_id.T

# extra = np.array([1,2,3,4,5]).reshape(-1,1) 
new_user = users_id.reshape(-1, 1)
users = np.hstack([users_likes,new_user])
# print(users)

print(users[coef==max_coef])
# np.append(users_likes,users_id,axis=1)
# print(users_likes)
