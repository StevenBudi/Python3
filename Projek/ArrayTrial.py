import numpy as np

#Matrix multiplication
try :
    array0 = np.array([(1, 3),(1, 2)],dtype=int)
    array1 = np.array([(1, 2),(1, 2)],dtype=int)
    newArray = array0.dot(array1)
    print(newArray)
except ValueError :
    print("Your Matrixs cannot be multiplied")

#Matriks inverse
try :
    m = np.matrix([[1, 2, 5], [1, 10, 7], [5, 6, 2]])
    inverse = m.I
    print(inverse)
except np.linalg.LinAlgError :
    print("Your matrix's is a Singular Matrix, it means it doesn't have an Inverse")
        
    


