# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
'''
For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def deleteDuplicates(head):
    if None == head or None == head.next:
        return head
    new_head = ListNode(-1)
    new_head.next = head
    parent = new_head
    cur = head
    while None != cur and None != cur.next:
        if cur.val == cur.next.val:
            val = cur.val
            while None != cur and val == cur.val:
                cur = cur.next
            parent.next = cur
        else:
            cur = cur.next
            parent = parent.next
    return new_head.next

l = ListNode(1)
l.next = ListNode(1)
l.next.next = ListNode(2)
l.next.next.next = ListNode(2)
l.next.next.next.next = ListNode(3)
h = deleteDuplicates(l)
print(h.val)
print(h.next.val)
print(h.next.next.val)
