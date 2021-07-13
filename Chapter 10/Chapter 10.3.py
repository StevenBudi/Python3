Data    = []
MyFile  = open("data1.txt", "r")
isi     = MyFile.read()
data    = isi.replace("|", " ")
data    = data.replace("\n", " ")
data    = data.split(" ")
data.remove("")

i = 0
for n in range(3):
    dataMhs = {}
    dataMhs["NIM"]  = data[i]
    i += 1
    dataMhs["Nama"] = data[i]
    i += 1
    dataMhs["Asal"] = data[i]
    i += 1
    Data.append(dataMhs)


print(Data)
MyFile.close()
