class Pegawai :
    def __init__(self, noPegawai, namaPegawai, status, anak):
        self.noPegawai      = int(noPegawai)
        self.namaPegawai    = namaPegawai.capitalize()
        self.status         = status.lower()
        self.anak           = int(anak)
        

    def hitungGajiPokok(self, masaKerja, golongan) :
        self.masaKerja      = int(masaKerja)
        self.golongan       = golongan.upper()
        if self.golongan == "A":
            if self.masaKerja < 10 :
                self.gaji = 3000000
            elif self.masaKerja >=10 and self.masaKerja <= 20 :
                self.gaji = 3500000
            else :
                self.gaji = 4000000
        elif self.golongan == "B":
            if self.masaKerja < 10 :
                self.gaji = 3750000
            elif self.masaKerja >= 10 and self.masaKerja <= 20 :
                self.gaji = 4250000
            else :
                self.gaji = 4750000
        elif self.golongan == "C":
            if self.masaKerja < 10 :
                self.gaji = 4500000
            elif self.masaKerja >= 10 and self.masaKerja <= 20 :
                self.gaji = 5000000
            else :
                self.gaji = 5500000
        else : 
            return "Golongan tidak valid"
        return self.gaji
       
    def hitungTunjanganIstri(self):
        if self.status == "sudah":
            self.tunjangan = self.gaji * 0.1
        else :
            self.tunjangan = 0
        return self.tunjangan
    
    def hitungTunjanganAnak(self):
        self.tunjanganAnak = self.anak*(self.gaji*0.05)
        return self.tunjanganAnak

    def hitungGajiKotor(self):
        self.kotor = self.gaji + self.tunjangan + self.tunjanganAnak
        return self.kotor

    def hitungPotongan(self):
        self.potongan = self.kotor*0.025
        return self.potongan

    def hitungGajiBersih(self):
        self.bersih = self.kotor - self.potongan
        return self.bersih

    def cetakStrukGaji(self):
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
        print("Tunjangan Anak   : ", "Rp".rjust(20) ,self.tunjanganAnak)
        print("-"*49, "+")
        print("Gaji Kotor       : ", "Rp".rjust(20) ,self.kotor)
        print("Potongan         : ", "Rp".rjust(20) ,self.potongan)
        print("-"*50)
        print("Gaji Bersih      : ", "Rp".rjust(20) ,self.bersih)


class Dosen(Pegawai):
    def __init__ (self, noPegawai, namaPegawai, status, anak, jabatanFungsional):
        Pegawai.__init__(self, noPegawai, namaPegawai, status, anak)
        self.jabatanFungsional = jabatanFungsional.capitalize()

    def tunjanganFungsional(self):
        if self.jabatanFungsional == "Lektor":
            self.tunjanganFungsional = self.gaji*0.5
        elif self.tunjanganFungsional == "Lektor Kepala" :
            self.tunjanganFungsional = self.gaji*0.8
        elif self.tunjanganFungsional == "Guru Besar":
            self.tunjanganFungsional = self.gaji*1.5
        else :
            self.tunjanganFungsional = 0
        return self.tunjanganFungsional



Data = Dosen(129, "Otong", "menikah", 5, "lektor")
    