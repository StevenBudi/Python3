#%%
import numpy as np

#%%
A = [1, 2, 3, 4, 5]
B = ["one", "two", "three", "four", "five"]
C = np.array(A + B)
C = C.reshape(2, 5)
print(sum(list(filter(lambda x : x> 3, A))))
print(np.array(B).dtype, np.array(A).dtype)
print(C, C.size, C.shape)
listD = np.array(B + A)
listD_arr = listD.reshape(2,5)

'''
np.concatenate axis = 1 is equal to hstack
               axis = 0 is equal to vstack

a shape = (x, y)
b shape = (a. b)
hstack y must same with b
vstack x must same with a
 
'''
#%%
E = np.vstack((C, listD_arr))
print(E, E.shape, E.size)

#%%
F = np.array([(1, 2, 3, 4, 5), (4, 6, 7, 8, 19)], dtype=int)
print(F[:, 0:3]*2)
print(F.reshape(-1, 1))
print(F.sum(axis=0))

mask = (F[:, :] != 5)
print(F[mask,])
# %%
