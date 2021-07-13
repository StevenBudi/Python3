#no. 11
Pay = 0
fruits = {"Apple" : 5000, "Orange" : 8500, "Manggo" : 7800, "Durian":6500}
while True:
    print("Menu :")
    print("A. Add fruit")
    print("B. Buy fruit")
    opt = str(input("Menu : "))
    opt.upper()
    if opt == "A":
        dict = fruits
        key  = str(input("Enter a fruit : "))
        if key in fruits:
            print("Fruit already exist")
            exit()
        value= int(input("Enter price : "))
        fruits[key] = value
        print(fruits)
    if opt == "B":
        while True :
            name = str(input("Enter a fruit : "))
            ammount  = int(input("Ammout         : "))
            print("-"*30)
            if name in fruits.keys():
                harga = fruits.get(name)
                total = harga*ammount
                Pay = Pay + total
            else:
                print("Data not found")
            opsi = str(input("Enter another (y/n)?: "))
            if opsi == "y":
                continue
            elif opsi == "n":
                print("Price Total       :", Pay)
                break