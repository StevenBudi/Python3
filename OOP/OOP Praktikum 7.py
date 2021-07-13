class Stack :
    def __init__(self):
        self.data = list()

    def push(self, value) :
        self.data.append(value)
        return self.data

    def pop(self):
        self.data.pop()
        return self.data

    def show (self):
        print(self.data)

Data = Stack()
Data.push(10)
Data.push(20)
Data.show()
Data.pop()
Data.show()