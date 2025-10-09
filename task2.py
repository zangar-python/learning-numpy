import numpy as np
import pandas as pd
activity = np.array([5, 12, 45, 0, 8, 30, 25, 60, 3, 18])

max = np.max(activity)
min = np.min(activity)

mean = np.mean(activity)

median = np.median(activity)


#print(max,mean,min,median)
print(f"max : {max} ; min :{min}")
print(f"mean : {mean} ; median : {median}")

activing = activity[activity>10]

low = activity[activity<10]
medium = activing[activing < 30]
hight = activity[30 <= activity]

print(f"activing users :{activing}")
print("")
print(f"low activity:{low}")
print("medium activity:",medium)
print("hight activity:",hight)



print("user 3:",activity[2])
print("user 6:",activity[5])
print("последний юзер:",activity[-1])


activity[activity==0] += 1
print(activity)

levels =[]
for i in activity:
    if i < 10:
        levels.append("low")
    elif 10 <= i < 30:
        levels.append("medium")
    else:
        levels.append("hight")
print(levels)



data_users_active = pd.DataFrame({
    "users_id":[i for i in range(1,len(activity)+1)],
    "activitys":activity,
    "levels":levels
})
print(data_users_active)

print("activngs:",data_users_active[data_users_active["levels"]=="hight"])
