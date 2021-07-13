import json

data = json.load(open("photos.json", "r"))

dataDict = {}
keySet = set()
for i in range(len(data)):
    keySet.add(data[i]["albumId"])

for key in keySet:
    dataDict[key] = 0

for j in range(len(data)):
    dataDict[data[j]["albumId"]] += 1

print(dataDict)
