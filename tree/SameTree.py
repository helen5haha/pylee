'''
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def insertLeft(self, node):
        if self.left == None:
            self.left = TreeNode(node)
        else:
            t = TreeNode(node)
            t.left = self.left
            self.left = t

    def insertRight(self, node):
        if self.right == None:
            self.right = TreeNode(node)
        else:
            t = TreeNode(node)
            t.right = self.right
            self.right = t

def isSameTree(p,q):
    if None == p and None == q:
        return True
    elif (None == p and None != q) or (None != p and None == q):
        return False
    else:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

r1 = TreeNode('a')
r1.insertLeft('c')
r2 = TreeNode('a')
r2.insertLeft('c')
isSameTree(r1, r2)