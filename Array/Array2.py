import numpy as np

# Random Array with 5x2 Size and value range from 100 to 200 with 10 increment betweeen value

np.random.seed(0)
arr1 = np.random.choice(np.arange(100, 200, 10), size=(5, 2))
print(arr1)