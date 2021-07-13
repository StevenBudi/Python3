#no. 3
list = []
data = int(input("Enter Loop Number : "))
for i in range(0, data):
    name = str(input("Enter Name : "))
    list.append(name)

list.sort
for j in list:
    print(j, "(",len(j),"characters",")")