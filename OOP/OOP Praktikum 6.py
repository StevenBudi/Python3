class BilanganRasional : 
    def __init__ (self, num1, num2):
        self.n1 = int(str(num1).split(".")[0])
        self.d1 = int(str(num1).split(".")[1])
        self.n2 = int(str(num2).split(".")[0])
        self.d2 = int(str(num2).split(".")[1])
        
    def penjumlahan(self):
        jumlah = (self.n1*self.d2 + self.n2*self.d1)/(self.d1*self.d2)
        print(jumlah)

    def pengurangan(self):
        kurang = (self.n1*self.d2 - self.n2*self.d1)/(self.d1*self.d2)
        print(kurang)

    def perkalian(self):
        kali = (self.n1*self.n2)/(self.d1*self.d2)
        print(kali)

    def pembagian(self):
        bagi = (self.n1*self.d2)/(self.d1*self.n2)
        print(bagi)

Angka = BilanganRasional(10.5, 3.7)
Angka.pembagian()
Angka.perkalian()
        