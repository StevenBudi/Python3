import numpy as np

#Array Reshape, Max, and Min

np.random.seed(0)
arr1 = np.random.randint(1, 200, 100)
arr2 = arr1.reshape(10, 10)
print(arr2)
print("="*100)
print("Max Value : ", arr2.max())
print("Min Value : ", arr2.min())