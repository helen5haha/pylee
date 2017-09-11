'''
Given a binary tree, return the preorder traversal of its nodes' values.
root - left - right
For example:
Given binary tree
   1
    \
     2
    /
   3
return [1,2,3].
Use stack: first right push, then left push
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

def preorderTraversal(root):
    if None == root:
        return []
    list = []
    stack = []
    cur = root

    while True:
        list.append(cur.val) ##
        if None != cur.right:
            stack.append(cur.right) ##
        if None != cur.left:
            stack.append(cur.left) ##
        if len(stack) >= 1:
            cur = stack.pop()
        else:
            break

    return list

r = TreeNode('1')
r.insertRight('2')
r.right.insertLeft('3')
preorderTraversal(r)