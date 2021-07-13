#no. 4
stuff = ["A", "B", "C", "D"]
while True :
    print(stuff)
    print("Menu :")
    print("A. Add stuff")
    print("B. Remove stuff")
    print("C. Show stuff")
    opt = str(input("Choose Menu : "))
    opt.upper()
    if opt == "A":
        new = str(input("var : "))
        stuff.append(new)
    try :
        if opt == "B":
            delete = str(input("var : "))
            stuff.remove(delete)
    except ValueError :
        print("Data not found")
    if opt == "C":
        print(stuff)
        break