Myfile = open("D:/bilangan.txt", "r")

for data in Myfile:
    pisah = data.split("|")
    hasil = int(pisah[0]) + int(pisah[1])
    print(hasil)
Myfile.close()