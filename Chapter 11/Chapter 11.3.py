from datetime import *
MyFile  = open("perpus.txt", "r")
isi     = MyFile.read()
data    = isi.replace("\n", "|")
data    = data.split("|")
def diffDate(x):
            x = x.split("-")
            x = date(int(x[0]), int(x[1]), int(x[2]))
            z = data[a+4].split("-")
            tanggal = date(int(z[0]), int(z[1]), int(z[2]))
            hasil = x - tanggal
            hasil = hasil.days
            return hasil
try:
    cari = str(input("Masukkan kode member: "))
    a = data.index(cari)
    if cari in data:
        print("Data Peminjaman Buku")
        print("Kode Member              : ", data[a] )
        print("Nama Member              : ", data[a+1])
        print("Judul Buku               : ", data[a+2])
        print("Tanggal Mulai Peminjaman : ", data[a+3])
        print("Tanggal Maks Peminjaman  : ", data[a+4])
        kembali = str(input("Tanggal Pengembalian     :  "))
        y = diffDate(kembali)
        if y > 0 :
            print("Terlambat                : ", y, "hari")
            denda = int(y)*2000
            print("Denda                    : ","Rp.", denda)
        else :
            print("Terima kasih telah mengembalikan buku tepat waktu")
except ValueError:
    print("Data member tidak ditemukan")


        