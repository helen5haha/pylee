'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
Mind to handle some reference that might be None
'''
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def deleteDuplicates(head):
    if None == head or None == head.next:
        return head
    cur = head
    while None != cur:
        if None != cur.next and cur.val == cur.next.val:
            cur.next = cur.next.next
            continue
        else:
            cur = cur.next
    return head

l = ListNode(1)
l.next = ListNode(1)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(3)
h = deleteDuplicates(l)
print(h.val)
print(h.next.val)
print(h.next.next.val)