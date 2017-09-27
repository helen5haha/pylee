'''
Given a binary tree
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set toNULL.
Initially, all next pointers are set to NULL.
Note:
You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
Similar to "Binary Tree Level Order Traversal", on base of it add the operation to hancle the next to NULL
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def connect(root):
    if None == root:
        return []
    reflist1 = [root]
    while True:
        reflist2 = []
        for i in range(0, len(reflist1)):
            cur = reflist1[i]
            if None != cur.left:
                reflist2.append(cur.left)
            if None != cur.right:
                reflist2.append(cur.right)
        if 0 == len(reflist2):
            break
        len_l = len(reflist2)
        for i in range(0, len_l - 1):
            reflist2[i].next = reflist2[i + 1]
        reflist2[len_l - 1].next = None
        reflist1 = reflist2

