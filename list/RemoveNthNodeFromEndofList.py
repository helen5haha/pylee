# Given a linked list, remove the nth node from the end of list and return its head
'''
For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
Solution: fast and slow pointers
Note that the node to delete might be the head, so create a fake head to "make" the head to non-head. :)
'''

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def removeNthFromEnd(head, n):
    if None == head:
        return head
    if None == head.next:
        return None
    new_head = ListNode(-1)
    new_head.next = head
    fast = new_head
    for i in range(0, n):
        if None != fast.next: ##
            fast = fast.next
        else:
            return head
    slow = new_head
    while None != fast.next: ##
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return new_head.next

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
h = removeNthFromEnd(l, 2)
print(h.val)
print(h.next.val)
print(h.next.next.val)