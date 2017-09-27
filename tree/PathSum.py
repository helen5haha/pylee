'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
Because we have to find all the solutions, we cannot prune in advance
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

paths = []

def doPathSum(root, total, sum, path):
    if None == root.left and None == root.right:
        path.append(root.val)
        result = (sum == (total + root.val))
        if True == result:
            paths.append(path)

    left = False
    right = False
    if None != root.left:
        new_path = path[:]
        new_path.append(root.val)
        left = doPathSum(root.left, total + root.val, sum, new_path)
    if None != root.right:
        new_path = path[:]
        new_path.append(root.val)
        right = doPathSum(root.right, total + root.val, sum, new_path)
    return left or right

def pathSum(root, sum):
    if None == root:
        return []
    result = doPathSum(root, 0, sum, [])
    return paths

r = TreeNode(5)
r.insertLeft(4)
r.insertRight(8)
r.left.insertLeft(11)
r.left.left.insertLeft(7)
r.left.left.insertRight(2)
r.right.insertLeft(13)
r.right.insertRight(4)
r.right.right.insertLeft(5)
r.right.right.insertRight(1)
pathSum(r, 22)