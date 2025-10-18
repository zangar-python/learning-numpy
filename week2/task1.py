import numpy as np

users_activity = np.random.randint(0,101,100)

class ControlActivity:
    def __init__(self,arr):
        self.arr = arr
        pass
    def activiting_users(self):
        random_activity = np.random.randint(0,len(self.arr),(len(self.arr)//10))
        return random_activity
    def set_activity(self,activity):
        # np.take(self.arr,activity,15)
        self.arr[activity] += 1000
        return len(activity)

users_list1 = ControlActivity(users_activity)
active = users_list1.activiting_users()
# print(active)
users_list1.set_activity(active)
phase_1 = users_list1.arr.copy()
print(phase_1)

users_list1.set_activity(users_list1.activiting_users())
phase_2 = users_list1.arr.copy()
print(phase_2)

# phase_1_indexes = np.where(phase_1>1000)[0]

phase_2_indexes = np.where(phase_2>1000)[0]
print(len(phase_2_indexes))
phase1_updated = np.where(phase_1>1000)[0]
phase2_updated = np.where(phase_2>1000)[0]
print(phase1_updated)
print(phase2_updated)
only_phase_2 = phase2_updated[np.isin(phase2_updated,phase1_updated,invert=True)]
print(only_phase_2)
print(phase_2[only_phase_2])
print("hello world")
