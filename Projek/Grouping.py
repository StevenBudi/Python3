import random
dataStundents = [0,1,2,3,4,5,6,7,8,9,10,11,12]

def grouping(data, groupNumber):
    random.shuffle(data)
    groupNumber = int(groupNumber)
    groups = [[] for _ in range(groupNumber)]
    lenght = len(data)//groupNumber
    for i in range(groupNumber):
        for _ in range(lenght):
            groups[i].append(data.pop(0))
    
    for j in range(len(groups)):
        print("Group " + str(j + 1)+ " = " + str(groups[j]))

    print("Misc")
    if len(data) != 0:
        for k in range(len(data)):
            print(str(data[k])+ " in to Group " + str(k + 1))


grouping(dataStundents, 3)

    

        



