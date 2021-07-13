class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def InsertData(self, value):
        if self.data:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.InsertData(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.InsertData(value)
        else:
            self.data = value

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=" ")
        if self.right:
            self.right.printTree()

    def invertTree(self, node):
        '''
        if not node:
            return
        else :
            #temp = node.left
            self.invertTree(node.left)
            self.invertTree(node.right)
            #node.left = node.right
            #node.right = temp
            node.left, node.right = node.right, node.left
        '''
        if node:
            node.left, node.right = node.right, node.left
            self.invertTree(node.left)
            self.invertTree(node.right)


root = Node(12)
root.InsertData(13)
root.InsertData(14)
root.InsertData(10)
root.InsertData(25)
root.InsertData(30)
root.printTree()
root.invertTree(root)
print()
root.printTree()
