MyFile  = open("data1.txt", "r")
isi     = MyFile.read()
data    = isi.replace("|", " ")
data    = data.replace("\n", " ")
data    = data.split(" ")
data.remove("")

try :
    cari = str(input("Masukkan NIM yang ingin dicari: "))
    a = data.index(cari)
    if cari in data:
        print("Data Mahasiswa")
        print("NIM    :", data[a])
        print("Nama   :", data[a + 1])
        print("Alamat :", data[a + 2])
except ValueError :
    print("Data mahasiswa tidak ditemukan")
    MyFile.close()