#no. 6

myData = ["Apple", "Durian", "Orange"]

def sortStringbyChar(x):
    list(x)
    x.sort(reverse = True, key=len)
    print(x)

sortStringbyChar(myData)