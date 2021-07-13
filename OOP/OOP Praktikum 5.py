class Subset :
    def __init__ (self):
        self.data = list()

    def addData(self , *Data):
        for i in Data:
            self.data.append(i)

    def slice(self):
        list_0 = [[]]
        for i in range(len(self.data) + 1):
            for j in range (i + 1, len(self.data) + 1):
                new = self.data[i:j]
                list_0.append(new)      
        return list_0

list_1 = Subset()
list_1.addData(0, 10, 20)
print(list_1.slice())
            
