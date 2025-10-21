import numpy as np 

users_likes = np.random.randint(0,2,size=(100,10))

user = [1,1,1,0,0,0,1,1,0,1]

user_norm = np.linalg.norm(user)
users_norm = np.linalg.norm(users_likes,axis=1)

cos_coef = (users_likes@user)/(user_norm*users_norm)
# cos_coef = users_likes@user

max_coef = np.max(cos_coef)

# print(users_likes)

print(users_likes[cos_coef==max_coef])

print(users_likes[np.all(users_likes == 1,axis=1)])
# print(cos_coef)