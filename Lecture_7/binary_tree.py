class Node:

    def  __init__(self,data):

        self.left = None
        self.right = None
        self.data = data

    def printTree(self):
        print(self.data)

root = Node(10)

root.printTree()

"""
    def inorderTraversal(self,root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self,root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

"""