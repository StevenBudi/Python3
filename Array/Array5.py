import numpy as np

# insert and delete a column

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sampleArray)
newColumn = np.array([10, 10, 10])
print(newColumn)

newArray = np.delete(sampleArray, 1, axis=1)
newArray = np.insert(newArray, 1, newColumn, axis=1)
print(newArray)

