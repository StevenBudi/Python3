from datetime import *
import numpy as np

now = datetime.now()

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()

print(year(now), month(now), day(now), time(now))

nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x>=3, nums)))
print(list(map(lambda y: y**2, nums)))

num = np.array([(1, 2, 3, 4, 5), (9, 3, 5, 8, 1)],dtype=int)
mask = (num[:,:] >= 3)
print(num[mask])