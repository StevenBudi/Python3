from itertools import combinations

listA = [0, 2, 3, 4, 5]

def subset(s, n, target):
    
    listC = []
    listB = list(combinations(s,n))
    for i in listB:
        if target == sum(i):
            listC.append(i)
    return listC

            


print(subset(listA, 3, 10))


