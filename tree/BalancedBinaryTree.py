'''
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1
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

def checkBBT(root):
    if None == root:
        return True, 0
    isLeftBBT, leftDepth = checkBBT(root.left)
    isRightBBT, rightDepth = checkBBT(root.right)
    isBBT = isLeftBBT and isRightBBT and abs(leftDepth - rightDepth) <= 1
    depth = max(leftDepth, rightDepth) + 1
    return isBBT, depth

def isBalanced(root):
    return checkBBT(root)[0]

r = TreeNode('3')
r.insertLeft('9')
r.insertRight('20')
r.right.insertLeft('15')
r.right.insertRight('7')
isBalanced(r)

