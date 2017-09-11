# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

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

def doSortedArrayToBST(num, start, end):
    if start > end:
        return None
    mid = start + (end - start) / 2
    root = TreeNode(num[mid]) #
    root.left = doSortedArrayToBST(num, start, mid - 1) #
    root.right = doSortedArrayToBST(num, mid + 1, end) #
    return root

def sortedArrayToBST(num):
    len_num = len(num)
    if 0 == len_num:
        return None
    return doSortedArrayToBST(num, 0, len_num - 1)

a = [1,2,3,4]
sortedArrayToBST(a)
