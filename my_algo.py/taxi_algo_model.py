import numpy as np

taxi = np.array([
    [10,2],
    [100,25]
])
task = np.array([
    [11,5],
    [10,24]
])


print(f"{taxi} - {task}")


res = taxi - task
mask = (res[:,1] < 2) & (res[:,1] > -2)

resu = taxi[mask].copy()  # ⚠️ копия, чтобы не изменять оригинал
resu[:,1] -= res[mask,1]  # вычитаем второй столбец res

print("Результат:")
# print(resu)
print(resu)


mask_2 = (res[:,0] < 2) & (res[:,0] > -2)

resu_2 = taxi[mask_2].copy()  # ⚠️ копия, чтобы не изменять оригинал
resu_2[:,0] -= res[mask_2,0]  # вычитаем второй столбец res

# print(f"{taxi} - {task}")
print(resu_2)


# print(taxi[(taxi[:,0]-task[:,0])<20])
# print(taxi[taxi[:,1]-task[:,1]<20])

