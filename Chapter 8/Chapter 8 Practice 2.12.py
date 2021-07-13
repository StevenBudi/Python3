#no. 12
Bayar = 0
buah = {"Apel" : 5000, "Jeruk" : 8500, "Mangga" : 7800, "Duku":6500}
while True :
    print("Menu :")
    print("A. Tambah data buah")
    print("B. Beli buah")
    print("C. Hapus buah")
    pilih = str(input("Pilihan Menu : "))
    pilih.upper()
    if pilih == "A":
        dict = buah
        key  = str(input("Masukkan nama buah  : "))
        if key in buah:
            print("Buah sudah ada")
        else :
            value= int(input("Masukkan harga buah : "))
            buah[key] = value
            print(buah)
    if pilih == "B":
        while True :
            nama = str(input("Masukkan nama buah : "))
            jml  = int(input("Berapa kg          : "))
            opsi = str(input("Beli buah yang lain(y/n)?: "))
            print("-"*30)
            if nama in buah.keys():
                harga = buah.get(nama)
                total = harga*jml
                Bayar = Bayar + total
            if opsi == "y":
                continue
            if opsi == "n":
                print("Total Harga        :", Bayar)
                break
    if pilih == "C":
        barang = str(input("Masukkan nama buah : "))
        if barang in buah.keys():
            del buah[barang]
        else :
            print("Nama buah tidak ditemukan")