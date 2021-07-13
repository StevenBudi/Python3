teks = "SAYA SUKA PYTHON"
list = list(teks)
key  = int(input("Masukkan key: "))

for data in list:
    hasil = (ord(data)+key)
    if data == " ":
        print(" ", end="")
        continue
    if hasil > ord("Z"):
        hasil -= 26
    elif hasil < ord("A"):
        hasil += 26
    print(chr(hasil),end = '')



