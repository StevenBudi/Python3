#no. 9

fruits = {"Apple" : 5000, "Orange" : 8500, "Manggo" : 7800, "Durian":6500}
name = str(input("Enter fruit name : "))
ammount = int(input("Ammount        : "))
print("-"*30)
if name in fruits.keys():
    harga = fruits.get(name)
    total = harga*ammount
    print("Total Price        :", total)
else :
    print("Data not found")