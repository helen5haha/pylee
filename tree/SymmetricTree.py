# Given a binary tree, check whether it is a mirror of itself
'''
For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
# Bonus point: solve it both recursively and iteratively
'''

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = TreeNode(newNode)
        else:
            t = TreeNode(newNode)
            t.left = self.left
            self.left= t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = TreeNode(newNode)
        else:
            t = TreeNode(newNode)
            t.right = self.right
            self.right = t

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRootVal(self, obj):
        self.val = obj

    def getRootVal(self):
        return self.val

def isSymmetric(root):
    if None == root:
        return True
    return checkSymmetric(root.getLeft(), root.getRight())

def checkSymmetric(left, right):
    if None == left and None == right:
        return True
    elif None == left or None == right:
        return False
    elif left.val != right.val:
        return False
    return checkSymmetric(left.getLeft(), right.getRight()) and checkSymmetric(left.getRight(), right.getLeft())

r1 = TreeNode('1')
r1.insertLeft('2')
r1.insertRight('2')
r1.getLeft().insertLeft('3')
r1.getRight().insertRight('3')
isSymmetric(r1)

