# Given a binary tree containing digits from 0-9 only, each root-to-lead path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123. Find the total sum of all root-to-leaf numbers
'''
For example,
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = 12 + 13 = 25.

Search Algorithm can be used to find at least one solution(DFS or BFS) or all solutions.
To find all solutions, there are two ways: from bottom to top and from top to bottom
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

# From bottom to top

def doSumNumbers1(root, val):
    if None == root.left and None == root.right:
        return val * 10 + root.val
    left = 0
    right = 0
    if None != root.left:
        left = doSumNumbers1(root.left, val * 10 + root.val)
    if None != root.right:
        right = doSumNumbers1(root.right, val * 10 + root.val)
    return left + right

def sumNumbers1(root):
    if None == root:
        return 0
    return doSumNumbers1(root, 0)

# From top to bottom
sum = 0

def doSumNumbers2(root, val):
    global sum
    if None == root.left and None == root.right:
        sum += val * 10 + root.val
    if None != root.left:
        doSumNumbers2(root.left, val * 10 + root.val)
    if None != root.right:
        doSumNumbers2(root.right, val * 10 + root.val)

def sumNumbers2(root):
    if None == root:
        return 0
    doSumNumbers2(root, 0)
    return sum

r = TreeNode(3)
r.insertLeft(9)
r.insertRight(20)
r.right.insertLeft(15)
r.right.insertRight(7)
sumNumbers2(r)
