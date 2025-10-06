import numpy as np

a = np.array([1,2,3])
b = np.array([
    [1,2,3],
    [4,5,6]
])

print(a)
print(b)

def massive_functions():
    print(a.ndim)#количество измерений
    print(b.ndim)#

    print(a.shape)#Тип расположения,типо сколько массивов и элементов
    print(b.shape)#


    print(b.dtype)#Тип int str float bool

#massive_functions() первый урок

def massive_operations(num):
    print("result")
    arr1=a + num #прибавить к каждому элементу num
    arr2 = b * num #умножить каждый элемент на num 
    print(arr1)
    print(arr2)
    
    print(np.mean(arr1))#среднее значение
    print(np.max(arr2))#максимально  значение
    return {
        "arr1":arr1,
        "arr2":arr2
    }

#res = massive_operations(5) базовые операций с массивами
print()
