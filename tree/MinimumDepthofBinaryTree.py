'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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

def recurMinDepth(root, depth):
    if None == root:
        return 0
    elif None == root.left and None == root.right:
        return 1

    left_depth = (recurMinDepth(root.left, depth) if None != root.left else 0)
    right_depth = (recurMinDepth(root.right, depth) if None != root.right else 0)

    # warn: a node just have a child, a node have two child, their height calculation method are different.
    if left_depth > 0 and right_depth > 0:
        return min(left_depth, right_depth) + 1;
    elif left_depth > 0:
        return left_depth + 1
    else:  # right_depth > 0, or (left_depth == 0 and right_depth == 0)
        return right_depth + 1 #

def minDepth(root):
    return recurMinDepth(root, 0)

r = TreeNode('3')
r.insertLeft('9')
r.insertRight('20')
r.right.insertLeft('15')
r.right.insertRight('7')
minDepth(r)