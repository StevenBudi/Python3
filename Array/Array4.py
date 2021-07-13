import numpy as np

# random array

np.random.seed(0)
arr1 = np.random.choice(np.arange(10, 30), size=(8, 3))
print(arr1)