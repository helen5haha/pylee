'''
Given a binary tree, return the inorder traversal of its nodes' values.
left - root - right (Postorder: left - right - root)
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?
if left.exist then push left(cur -> left.left) else pop(output pop, if pop has right, cur -> right)
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

def inorderTraversal(root):
    if None == root:
        return []
    list = []
    stack = []
    cur = root
    stack.append(cur) #

    while True:
        if None != cur and None != cur.left:
            stack.append(cur.left) #
            cur = cur.left #
            continue
        if len(stack) >= 1:
            cur = stack.pop() #
            list.append(cur.val) #
            cur = cur.right #
        else:
            break
        if None != cur:
            stack.append(cur)
    return list


r = TreeNode('1')
r.insertRight('2')
r.right.insertLeft('3')
inorderTraversal(r)