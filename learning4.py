import numpy as np
import pandas as pd

class UserActivity:
    activity = []
    def __init__(self):
        pass
    def set_arr_activity(self):
        self.activity = np.random.randint(1,100,size=(10))
        return self.activity
    #def set_data(self):
        #data ={
           # "activity":self.activity,
           # "id":[i for i in range(1,len(self.activity)+1)],
                        
            #"low":self.activity[self.activity <30],
            #"medium":self.activity[(self.activity >= 30) & (self.activity<70)],
            #"hight":self.activity[self.activity >= 70]
            
       # }
        #df = pd.DataFrame(data)
        #return df
users_data = UserActivity()
arr = users_data.set_arr_activity()
arr2 = users_data.set_arr_activity()
arr3 = np.sort(np.hstack((arr,arr2)))
#data = users_data.set_data()
#print(data)
level = np.full(len(arr3),"low")

level[(arr3 > 30)&(arr3 <= 70)] = "medium"
level[arr3 >=70]= "hight"
data ={
    "activity":arr3,
    "status":level
}
df = pd.DataFrame(data)
print(df)

