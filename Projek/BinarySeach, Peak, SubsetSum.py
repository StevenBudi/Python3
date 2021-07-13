def binarySearch(arr, num):
    # Dalam Binary Search list harus urut
    arr.sort()
    listSize = len(arr)
    
    lowpoint = 0
    highpoint = listSize-1
    

    while lowpoint <= highpoint:
        midpoint = (lowpoint+highpoint)//2

        if arr[midpoint] == num:
            return midpoint
        
        elif num > arr[midpoint]:
            lowpoint = midpoint + 1
        else :
            highpoint = midpoint - 1

    if lowpoint > highpoint:
        return None

peak = [25, 34, 67, 80, 3, 5, 78, 90, 100, 25, 12]

print(binarySearch(peak, 12))

def findPeakElement(arr):
    return find(arr, 0, len(arr)-1)

def find(arr, low, high):
    if (low == high):
        return low
    midpoint = (low+high)//2
    if arr[midpoint] > arr[midpoint+1]:
        return find(arr, low, midpoint)
    return find(arr, midpoint+1, high)

print(findPeakElement(peak))


def isSubsetSum(arr, n, sum):

    #Base Cases
    if sum == 0:
        return True
    elif sum != 0 and n == 0:
        return False
    
    if arr[n-1] > sum :
        return isSubsetSum(arr, n-1, sum)

    return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])

print(isSubsetSum(peak, len(peak), 50))

