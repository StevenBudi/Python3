import math
class Lingkaran:
    def __init__(self,jari2):  
        self.jari2 = jari2

    def hitungLuas(self):
        luas = math.pi*self.jari2**2
        return luas

    def hitungKeliling(self):
        keliling =  math.pi*self.jari2*2
        return keliling

    def luasJuring(self, sudut):
        self.sudut = sudut
        juring = (self.sudut/360)*math.pi*self.jari2**2
        return juring
        


lingk1 = Lingkaran(10)
print(lingk1.hitungLuas())
print(lingk1.hitungKeliling())
print(lingk1.luasJuring(120))

