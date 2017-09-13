'''
Sort a linked list using insertion sort.
Two ways:
1 - create new list, every time insert a node into it
2 - add a condition check(when already sorted, do nothing), do it in-place
'''

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def insertionSortList(head):
    if None == head or None == head.next:
        return head

    new_head = ListNode(0)
    new_head.next = head

    last = new_head.next
    cur = new_head.next.next
    while None != cur:
        if new_head != last and cur.val >= last.val:
            last = cur
            cur = cur.next
            continue
        ins = new_head
        while None != ins.next and ins.next.val <= cur.val:  # stable sort
            ins = ins.next
        next_cur = cur.next
        last.next = cur.next
        cur.next = ins.next
        ins.next = cur
        cur = next_cur

    return new_head.next

l = ListNode(3)
l.next = ListNode(19)
l.next.next = ListNode(5)
l.next.next.next = ListNode(1)
l.next.next.next.next = ListNode(16)
h = insertionSortList(l)
print(h.val)
print(h.next.val)
print(h.next.next.val)
print(h.next.next.next.val)
print(h.next.next.next.next.val)