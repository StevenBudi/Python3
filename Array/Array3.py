import numpy as np
import math

# Array operation

arrayOne = np.array(([[5, 6, 9], [21, 18, 27]]),dtype=float)
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

arraySum = arrayOne + arrayTwo
print(arraySum)

for x in range(len(arraySum)):
    for y in range(len(arraySum[x])):
        arraySum[x, y] = math.sqrt(arraySum[x, y])

print(arraySum)