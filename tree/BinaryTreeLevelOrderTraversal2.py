'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
Use queue, or two stacks
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

def levelOrder(root):
    if None == root:
        return [ ]
    results = [[root.val]]
    reflist1 = [root]

    while True:
        reflist2 = [ ]
        result = [ ]
        for i in range(0, len(reflist1)):
            cur = reflist1[i]
            if None != cur.left:
                reflist2.append(cur.left)
                result.append(cur.left.val)
            if None != cur.right:
                reflist2.append(cur.right)
                result.append(cur.right.val)
        if 0 == len(reflist2):
            break
        results.append(result)
        reflist1 = reflist2
    return results


r = TreeNode('3')
r.insertLeft('9')
r.insertRight('20')
r.right.insertLeft('15')
r.right.insertRight('7')
levelOrder(r)