import math
from statistics import mode
class Statistik :
    def __init__(self):
        self.data = list()
    
    def addData(self, *Data):
        for i in Data:
            self.data.append(i)

    def maksimum(self):
        maks = max(self.data)
        return maks

    def minimum(self):
        minim = min(self.data)
        return minim

    def rerata(self):
        rata = sum(self.data)/len(self.data)
        return rata

    def Modus(self):
        modus = mode(self.data)
        return modus

Data = Statistik()
Data.addData(10, 20, 30, 10, 20 ,30, 40, 20)
print(Data.maksimum())
print(Data.minimum())
print(Data.rerata())
print(Data.Modus())
