myFile = open("dataKaryawan.dat", "r")
isi = myFile.read()
data = isi.replace("\n", "|")
data = data.split("|")
data.remove('')

def getGapok(x):
    gaji = 0
    if x == "A":
        gaji = 4000000
        return gaji
    if x == "B":
        gaji = 4500000
        return gaji
    if x == "C":
        gaji = 5000000
        return gaji
    else :
        print("Golongan tidak valid")
print("-" * 100)
print("Kode Kary".ljust(10), "Nama Kary".ljust(10), " Alamat".rjust(12), "Gol".rjust(5), "GajiPokok".rjust(10), "TglLahir".ljust(10), "Usia".rjust(5))
print("-" * 100)
n = 0
for i in range(len(data)// 6):
    kode = data[n]
    nama = data[n+1]
    almt = data[n+2]
    gol  = data[n+3]
    gaji = str(getGapok(gol))
    tggl = data[n+4]
    usia = data[n+5]
    print(kode.ljust(10), nama.ljust(15), almt.ljust(10), gol.ljust(5), gaji.rjust(5), tggl.ljust(5), usia.rjust(5))
    n += 6
print("-" * 100)