class Pasangan :
    def __init__ (self):
        self.data = list()

    def addData(self, *Data):
        for i in Data :
            self.data.append(i)

    def target (self, value):
        self.value = value

    def find(self):
        m = 0
        n = 1
        while True :
            if self.data[m] + self.data[n] == self.value:
                return [m, n]
            else :
                m += 1
                n += 1

list_1 = Pasangan()
list_1.addData(0, 10, 70 , 50, 40, 20, 30)
list_1.target(80)
print(list_1.find())