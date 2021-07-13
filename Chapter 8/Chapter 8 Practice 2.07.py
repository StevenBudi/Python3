#no. 7

fruits = {"Apple" : 5000, "Orange" : 8500, "Manggo" : 7800, "Durian":6500}
data = list(fruits.values())
data2 =list(fruits.keys())
print(data2[data.index(max(data))])