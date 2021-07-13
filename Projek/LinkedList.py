class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def PrintLinkedList(self):
        def decorator():
            return "->"
        counter = 1
        value = self.head
        while value:
            print(value.data, decorator(), end=" ")
            value = value.next
            counter += 1
        print(None)
        print("Banyaknya Node saaat ini : {}\n".format(counter))

    # Menambahkan Data pada Tail
    def AddData(self, data):
        value = self.head
        # Memasukkan data saat node.next == null/None
        while value.next != None:
            value = value.next
        dataName = Node(data)
        # Mengubah node.next yg kosong menjadi data yang baru dimasukkan
        value.next = dataName

        return Node

    def DeleteData(self, data):
        value = self.head
        '''
        Skema DeleteData
        a -> b -> c -> d
        a -> b -> c -> d #ex found c, temp = b, value = b
        value = value.next # value = c
        temp.next = value.next #  b.next = d
        '''
        while True :
            # Mencari data pada linked list
            if value.next.data != data:
                value = value.next
            else:
                # Menyimpan data pada node sebelumnya
                temp = value

                break
        # bergeser ke node selanjutnya
        value = value.next
        # menggeser temp.next menjadi value.next
        temp.next = value.next
        value.next = None

    def ReverseList(self):
        currentNode = self.head
        previousNode = None
        nextNode = currentNode.next

        # a -> b -> c -> d
        # d -> c -> b -> a
        '''
        Skema ReverseList
        a -> b -> c -> d
        a -> None #1 curr = a, prev = None, next = b
        b -> a -> None #2 curr = b, prev = a, next = c
        c -> b -> a -> None #3 curr = c, prev = b, next = d
        d -> c -> b -> -> a -> None #4 curr = d, prev = c, next = None
        #5 curr = None (break loop), prev = d, next = None
        '''
        while currentNode:
            # Mengubah lengan antar node
            currentNode.next = previousNode

            # Ubah node sebelumnya menjadi node sekarang
            previousNode, currentNode = currentNode, nextNode
            # Ubah next node menjadi nexNode.next selama nextNode tidak None
            if nextNode:
                nextNode = nextNode.next
        # Menjadikan data terakhir sebagai head
        self.head = previousNode

    # Menambahkan Data pada Head
    def InsertData(self, data):
        temp, temp.next = self.head, self.head.next
        self.head = Node(data)
        self.head.next = temp

'''
Data di head tidak boleh dihapus, apabila dihapus maka akan mengakibatkan error        
'''

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node(1)
    linkedList.AddData(20)
    linkedList.AddData(13)
    linkedList.AddData(15)
    linkedList.AddData(7)
    linkedList.AddData(6)
    linkedList.DeleteData(13)
    linkedList.PrintLinkedList()
    linkedList.ReverseList()
    linkedList.PrintLinkedList()
    linkedList.InsertData(7)
    linkedList.PrintLinkedList()
