#no. 10
Paid = 0
fruits = {"Apple" : 5000, "Orange" : 8500, "Manggo" : 7800, "Durian":6500}
while True :
    name = str(input("Enter fruit name : "))
    ammount  = int(input("Ammount          : "))
    opt = str(input("Enter another (y/n)?: "))
    opt.lower()
    print("-"*30)
    if name in fruits.keys():
        price = fruits.get(name)
        total = price*ammount
        Paid = Paid + total
    if opt == "y":
        continue
    if opt == "n":
        print("Total Price        :", Paid)
        break