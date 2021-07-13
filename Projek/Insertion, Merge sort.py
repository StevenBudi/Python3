def InsertionSort(A) :
    n = len(A)
    temp = 0
    #loop on array
    for i in range(1, n):
        temp = A[i]
        # set pointer
        j = i -1
        #check array position not at 0 and if Array[j] is lesser than it's previous indexes value
        while j >= 0 and temp < A[j]:
            A[j+1] = A[j]
            #move pointer backward
            j -= 1
        A[j+1] = temp 
    return A

print(InsertionSort([2,13,5,18,16,3]))

def mergeSort(data):
    #check if array length isn't 1
    #base case
    if len(data) > 1 :
        mid = len(data)//2

        #split data into 2 sides
        L = data[:mid]
        R = data[mid:]

        #recursive
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            #compare two values on two different lists
            if L[i] < R[j]:
                #replace the value on the original list
                data[k] = L[i]
                i += 1
            else :
                data[k] = R[j]
                j+= 1
            k += 1
        
        # residual value on the L and R list
        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1
    return data

print(mergeSort([0, 2, 7, 5, 1, 3, 12, 8, 6, 3, 9, 1]))


