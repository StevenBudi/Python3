import math
room = 4
roomLength = 4*100
roomWidth = 4*100
roomArea = room*roomLength*roomWidth
ceramicLength = 40
ceramicWidth = 30
ceramicArea = ceramicLength*ceramicWidth
ceramicCount = roomArea/ceramicArea
print(ceramicCount)
box = math.ceil(ceramicCount/5)
backup = math.ceil(10*box/100)
total = box+backup
cost = total*125000
print(cost)