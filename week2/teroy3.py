import numpy as np

# Создадим выборку: рост и вес
height = np.random.normal(170, 10, 1000)
weight = height * 0.45 + np.random.normal(0, 5, 1000)

# Ковариация
print("Ковариация:")
print(np.cov(height, weight))

# Корреляция (более нормализованная)
print("Корреляция:")
print(np.corrcoef(height, weight))