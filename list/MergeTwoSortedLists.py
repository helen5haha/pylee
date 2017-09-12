'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def mergeTwoList(l1,l2):
    if None == l1 and None == l2:
        return None
    elif None == l1:
        return l2
    elif None == l2:
        return l1
    new_list = ListNode(0)
    cur = new_list
    node1 = l1
    node2 = l2
    while None != node1 and None != node2:
        if node1.val < node2.val:
            cur.next = node1
            node1 = node1.next
        else:
            cur.next = node2
            node2 = node2.next
        cur = cur.next
    if None != node1:
        cur.next = node1
    else:
        cur.next = node2
    return new_list.next

l1 = ListNode(1)
l1.next = ListNode(3)
l2 = ListNode(2)
l2.next = ListNode(4)
h = mergeTwoList(l1, l2)
print(h.val)
print(h.next.val)
print(h.next.next.val)
print(h.next.next.next.val)

