class Node:

    def  __init__(self,data):

        self.left = None
        self.right = None
        self.data = data

    def findval(self,lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + "Not found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + "Not found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data)+"is found")

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()


root = Node(10)
root.findval(6)

root.printTree()