'''
Given a binary tree, flatten it to a linked list in-place.
For example,
Given
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Hints: If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
Preorder to be a linked list, then postorder traverse it:
first flatten the left, insert it between the current node and its direct rightChild, and then flatten the right
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

def flatten(root):
    if None == root:
        return
    if None != root.left:
        flatten(root.left) #
    if None != root.right:
        flatten(root.right) #
    left = root.left
    right = root.left
    while None != right and None != right.right:
        right = right.right
    if None != right:
        right.right = root.right
    if None != left:
        root.right = left
    root.left = None

r = TreeNode('3')
r.insertLeft('9')
r.insertRight('20')
r.right.insertLeft('15')
r.right.insertRight('7')
flatten(r)






























