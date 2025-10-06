#Задача 1
import numpy as np
import pandas as pd
 
users = np.array([23, 17, 8, 45, 0, 13])
 
class UsersActiveControl:
    def __init__(self,users_active):
         self.users_active = users_active
         pass
    def mean_active(self):
        return np.mean(self.users_active)
    def active_filter(self):
        data ={
            "active":self.users_active
        }
        df = pd.DataFrame(data)
        return df[df["active"]>10]
    def data_frame(self): 
         data ={
             "user_id":[1,2,3,4,5,6],
             "activity":self.users_active
         }
         df = pd.DataFrame(data)
         status = (df["activity"] > 10).tolist()
         status_arr =[]
         for i in status:
             if i:
                 status_arr.append("active")
             else:
                 status_arr.append("inactive")
         df["status"] = status_arr
         #print(df["status"])
         return df
         
   
user_active = UsersActiveControl(users)
print(user_active.mean_active())
print(user_active.active_filter())
print(user_active.data_frame())
