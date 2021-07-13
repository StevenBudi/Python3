#no. 1
list = []
data = int(input("Enter Loop Number : "))
for i in range(0, data):
    angka = int(input("Enter Number: "))
    list.append(angka)

list.sort(reverse=True)
print(list)




