import math
class common :
    def __init__(self):
        self._value = []

    def setData(self, *value):
        for data in value:
            if data == 0:
                return False
            self._value.append(data)

    def getData(self):
        return self._value

    #Least Common Multiple
    def least(self):
        factors = [[]for _ in range(len(self._value))]
        j = 0
        #Creating Factors Tree
        #Stolen Code (Don't Ask me IDK what it means)
        for data in self._value:
            while data % 2 == 0:
                factors[j].append(2)
                data = data / 2
            for i in range(3, int(math.sqrt(data))+1, 2):
                while data % i == 0:
                    factors[j].append(i)
                    data = data/i
            if data > 2 :
                factors[j].append(data)
            j += 1  
        #Stolen Code (Don't Ask me IDK what it means)
        multiplier = {}
        for k in range(len(factors)):
            for l in factors[k]:
                multiplier[l] = 0
            
        for m in range(len(factors)):
            for n in factors[m]:
                counter = factors[m].count(n)
                data = {n : counter}
                if counter > multiplier.get(n):
                    multiplier.update(data)

        leastMultiply = 1
        for key in multiplier:
            result = key**(multiplier.get(key))
            leastMultiply *= result
        return int(leastMultiply)


    #Greatest Common Multiple
    def greatest(self):
        factors = [[] for _ in range(len(self._value))]
        j = 0
        for data in self._value:
            for i in range(1, data+1):
                if data % i == 0:
                    factors[j].append(i)
            j += 1
        
        for k in range(len(factors)):
            factors[k] = set(factors[k])

        sameFactors = set.intersection(*factors)
        sameFactors = list(sameFactors)
        return sameFactors[len(sameFactors) - 1]

Num = common()
Num.setData(100, 25, 60, 28)
print(Num.greatest())
print(Num.least())      
