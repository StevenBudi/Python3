import math        
class Kombinatronik :
    def __init__(self):
        self.m = None
        self.n = None
        

    def faktorial(self, value):
        self.value = value
        if value <= 1:
            return 1
        else :
            return value * self.faktorial(value - 1) 

    def kombinasi(self, m, n):
        self.m = m
        self.n = n
        if self.m > self.n :
            kombi = self.faktorial(m)//(self.faktorial(n)*self.faktorial(m-n))
            return kombi
        else :
            return "Angka pertama harus lebih besar"
        
    def permutasi(self, m, n):
        self.m = m
        self.n = n
        if self.m > self.n :
            mutasi = self.faktorial(m)//self.faktorial(m-n)
            return mutasi
        else : 
            return "Angka pertama harus lebih besar"

    def siklis(self, m):
        self.m = m 
        sik = self.faktorial(m - 1)
        return sik

data = Kombinatronik()
print(data.permutasi(10,8))
print(data.siklis(5))
print(data.kombinasi(10,8))

