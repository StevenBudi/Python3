class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def AddNode(self, data):
        value = self.head
        while value.next:
            value = value.next

        dataName = Node(data)
        value.next = dataName
    
    def DeleteNode(self, data):
        value = self.head
        while True:
            if data != value.next.data :
                value = value.next
            else :
                temp = value
                break

        value = value.next
        temp.next = value.next

    def ReverseList(self):
        currentNode = self.head
        previousNode = None
        nextNode = currentNode.next

        while currentNode:
            currentNode.next = previousNode

            previousNode = currentNode
            currentNode = nextNode
            if nextNode.next:
                nextNode = nextNode.next

        self.head = previousNode


    def PrintList(self):
        value = self.head
        counter  = 1
        while value:
            value = value.next
            counter += 1
            print(value)