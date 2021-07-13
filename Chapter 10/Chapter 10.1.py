import os
os.chdir("C:\\Users\ASUS\Documents\Python\Chapter 10")
file = open("data.txt", "r")
i = 0
j = 0
for data in file:
    data = int(data)
    if data%2==0:
        i += 1
    else :
        j += 1

print("Jumlah Bilangan Genap adalah", i)
print("Jumlah Bilangan Ganjil adalah", j)
