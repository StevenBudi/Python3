def atas(n):
    for i in range(n):
        bintangAtas = ("* " * (2*i+1))
        print(bintangAtas.center(20))

def bawah(n):
    for i in range(n):
        bintangBawah = ("* " * (n*2-1-(2*i)))
        print(bintangBawah.center(20))

import math
n = int(input("Masukkan bilangan : "))
if n%2 == 1:
    atas(math.ceil(n/2))
    bawah(math.floor(n/2))
else :
    print("Bilangan harus ganjil")
    




