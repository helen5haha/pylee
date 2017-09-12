# Sort a linked list in O(n log n) time using constant space complexity.

class ListNode:
    def __init__(self,value):
        self.val = value
        self.next = None

def findMiddle(head):
    slow = head
    fast = head.next
    while None != fast and None != fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def mergeList(head):
    if None == head.next:
        return head
    mid = findMiddle(head)
    right_head = mid.next
    mid.next = None
    left_list = mergeList(head)
    right_list = mergeList(right_head)
    new_head = ListNode(-1)
    new_tail = new_head
    left_node = left_list
    right_node = right_list
    while None != left_node and None != right_node:
        if left_node.val <= right_node.val:
            new_tail.next = left_node
            left_node = left_node.next
        else: # left > right
            new_tail.next = right_node
            right_node = right_node.next
        new_tail = new_tail.next
    new_tail.next = left_node if None != left_node else right_node
    return new_head.next

def sortList(head):
    if None == head:
        return None
    return mergeList(head)

l = ListNode(3)
l.next = ListNode(9)
l.next.next = ListNode(1)
l.next.next.next = ListNode(0)
l.next.next.next.next = ListNode(8)
h = sortList(l)

