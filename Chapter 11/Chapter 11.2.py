from datetime import *
Myfile = open("perpus.txt", "a")
while True :
    kode  = str(input("Masukkan Kode Member : "))
    nama = str(input("Masukkan Nama Member : "))
    buku = str(input("Judul Buku           : "))
    now = datetime.date(datetime.now())
    balik = now + timedelta(days=7)
    Myfile.write("|".join([kode, nama, buku, str(now), str(balik)]))
    Myfile.write("\n")
    opsi = str(input("Ulangi input lagi? (y/n): "))
    if opsi == "y" :
        continue
    else :
        Myfile.close()
        MFile = open("perpus.txt", "r")
        Cetak = MFile.read()
        print(Cetak)
        break
