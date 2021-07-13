import math
room = 4
roomLength = 4*100
roomWidth = 4*100
roomArea = room*roomLength*roomWidth
ceramicLength = 40
ceramicWidth = 30
ceramicArea = ceramicLength*ceramicWidth
ceramicCount = roomArea/ceramicArea
print("Ceramic needed : ",ceramicCount)
box = math.ceil(ceramicCount/5)
print("Box needed : ", box)