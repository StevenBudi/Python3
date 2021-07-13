Myfile = open("data1.txt", "a")
while True :
    nim  = str(input("Masukkan NIM : "))
    nama = str(input("Masukkan Nama Mhs : "))
    asal = str(input("Masukkan Asal : "))
    Myfile.write("|".join([nim, nama, asal]))
    Myfile.write("\n")
    opsi = str(input("Ulangi input lagi? (y/n): "))
    if opsi == "y" :
        continue
    else :
        Myfile.close()
        MFile = open("data1.txt", "r")
        Cetak = MFile.read()
        print(Cetak)
        break
