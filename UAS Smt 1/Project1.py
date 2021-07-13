from datetime import*
def getUsia(n):
    x = n.split("-")
    x = date(int(x[0]), int(x[1]), int(x[2]))
    y = datetime.date(datetime.now())
    z = y - x
    z = z.days
    z = z // 365
    return z

def addKaryawan():
    while True :
        myFile = open("D:/data.dat", "a")
        nip  = str(input("Masukkan NIP                  : "))
        nama = str(input("Masukkan Nama                 : "))
        almt = str(input("Masukkan Alamat               : "))
        gol  = str(input("Masukkan Golongan(A/B/C)      : "))
        gol  = gol.upper()
        tgl  = str(input("Masukkan Tgl Lahir(YYYY-MM-DD): "))
        usia = str(getUsia(tgl))
        myFile.write("|".join([nip, nama, almt, gol, tgl, usia]))
        myFile.write("\n")
        print("=" * 100)
        opsi = str(input("Tambah data(y/n)? : "))
        print("=" * 100)
        opsi =opsi.lower()
        print("=" * 100)
        if opsi == "y":
            continue
        else :
            myFile.close()
            my_File = open("D:/data.dat", "r")
            cetak  = my_File.read()
            print(cetak)
            my_File.close()
            break


print("===Data Karyawan===")
addKaryawan()



        
    
