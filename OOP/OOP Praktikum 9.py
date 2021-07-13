class Pegawai :
    def __init__(self):
        self.noPegawai      = None
        self.namaPegawai    = None
        self.status         = None
        self.anak           = None
        self.masaKerja      = None
        self.golongan       = None

    def setData(self):
        self.noPegawai   = str(input("Masukkan No. Pegawai    : "))
        self.namaPegawai = str(input("Masukkan Nama Pegawai   : "))

    def hitungGajiPokok(self):
        self.masaKerja   = int(input("Masukkan masa kerja     : "))
        self.golongan    = str(input("Masukkan golongan       : "))
        golongan = self.golongan.upper()
        if golongan == "A":
            if self.masaKerja < 10 :
                self.gaji = 3000000
            elif self.masaKerja > 10 and self.masaKerja < 20 :
                self.gaji = 3750000
            else :
                self.gaji = 4500000
        elif golongan == "B":
            if self.masaKerja < 10 :
                self.gaji = 3500000
            elif self.masaKerja > 10 and self.masaKerja < 20 :
                self.gaji = 4250000
            else :
                self.gaji = 5000000
        elif golongan == "C":
            if self.masaKerja < 10 :
                self.gaji = 4000000
            elif self.masaKerja > 10 and self.masaKerja < 20 :
                self.gaji = 4750000
            else :
                self.gaji = 5500000
        else : 
            print("Golongan tidak valid")
        print(self.gaji)
    
    def hitungTunjanganIstri(self):
        self.status      = str(input("Sudah Menikah/Belum ?   : "))
        self.status_0 = self.status.lower()
        if self.status_0 == "sudah":
            self.tunjangan = self.gaji*0.1
            print(self.tunjangan)
        elif self.status_0 == "belum":
            self.tunjangan = 0
            print(self.tunjangan)
        else :
            print("Status tidak valid")

    def TunjanganAnak(self):
        if self.status_0 == "sudah":
            self.anak    = int(input("Masukkan jumlah anak    : "))
            self.tunjangan_1 = self.gaji*0.05*self.anak
            print(self.tunjangan_1)
        else :
            self.tunjangan_1 = 0
            print(self.tunjangan_1)
        
    def gajiKotor(self):
        self.Kotor = self.gaji+self.tunjangan+self.tunjangan_1
        print(self.Kotor)

    def hitungPotongan(self):
        self.potongan = self.Kotor*0.025
        print(self.potongan)

    def gajiBersih(self):
        self.Bersih = self.Kotor - self.potongan
        print(self.Bersih)

    def cetakStruk(self):
        print("="*50)
        print("Struk", end= " ")
        print("Gaji".center(25), end= " ")
        print("Pegawai".rjust(10))
        print("-"*50)
        print("Nama Pegawai     : " , self.namaPegawai.capitalize(), end=" ")
        print("(", "No. Pegawai: ".rjust(22), self.noPegawai, ")")
        print("Status Menikah   : ", self.status.capitalize().rjust(30))
        print("Jumlah Anak      : ", str(self.anak).rjust(30))
        print("Masa Kerja       : ", self.masaKerja," Tahun")
        print("-"*50)
        print("Gaji Pokok       : ", "Rp".rjust(20) ,self.gaji)
        print("Tunjangan Istri  : ", "Rp".rjust(20) ,self.tunjangan)
        print("Tunjangan Anak   : ", "Rp".rjust(20) ,self.tunjangan_1)
        print("-"*49, "+")
        print("Gaji Kotor       : ", "Rp".rjust(20) ,self.Kotor)
        print("Potongan         : ", "Rp".rjust(20) ,self.potongan)
        print("-"*50)
        print("Gaji Bersih      : ", "Rp".rjust(20) ,self.Bersih)

class Dosen(Pegawai):
    def __init__(self):
        Pegawai.__init__(self)

    def jabatanFungsional(self):
        self.jabatan = str(input("Masukkan Jabatan : "))
        print(self.jabatan.capitalize())

    def tunjanganFungsional(self):
        jabatan = self.jabatan.lower()
        if jabatan == "lektor":
            self.tunjangan_2 = self.gaji*0.5
        elif jabatan == "lektor kepala":
            self.tunjangan_2 = self.gaji*0.8
        elif jabatan == "guru besar":
            self.tunjangan_2 = self.gaji*1.5
        print(self.tunjangan_2.capitalize())

Data = Dosen()
Data.setData()
Data.hitungGajiPokok()
Data.hitungTunjanganIstri()
Data.TunjanganAnak()
Data.gajiKotor()
Data.hitungPotongan()
Data.gajiBersih()
Data.jabatanFungsional()
Data.tunjanganFungsional()
        