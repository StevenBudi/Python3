myFile = open("dataKaryawan.dat", "r")
isi    = myFile.read()
data   = isi.replace("\n", "|")
data   = data.split("|")
data.remove('')
data_1 = {}

n = 0
for i in range(len(data)//6):
    data_1[data[n]] = (data[n+1], data[n+2], data[n+3], data[n+4], data[n+5])
    n += 6


def getGapok(x):
    gaji = 0
    if x == "A":
        gaji = 4000000
        return gaji
    elif x == "B":
        gaji = 4500000
        return gaji
    elif x == "C":
        gaji = 5000000
        return gaji
    else :
        print("Golongan tidak valid")
try :
    print("======Data Karyawan======")
    cari = str(input("Masukkan Kode Karyawan : "))
    hasil = data_1.get(cari)
    hasil = list(hasil)
    print("Kode Karyawan : ", cari)
    print("Nama Karyawan : ", hasil[0])
    print("Alamat        : ", hasil[1])
    print("Golongan      : ", hasil[2])
    print("Gaji Pokok    : ", "Rp.",getGapok(hasil[2]))
    print("Tanggal Lahir : ", hasil[3], "(",hasil[4],"tahun",")")
except :
    print("Data tidak ditemukan")









