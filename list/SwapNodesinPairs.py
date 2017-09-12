'''
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
Note that the length of the linked list might be odd, so don't forget to check whether the second_node is None
'''

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def swapPairs(head):
    if None == head:
        return head
    new_head = ListNode(0)
    new_head.next = head
    last_node = new_head

    while True:
        first_node = last_node.next
        if None == first_node:
            break
        second_node = first_node.next
        if None == second_node:
            break
        last_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        last_node = first_node
    return new_head.next

l = ListNode('1')
l.next = ListNode('2')
l.next.next = ListNode('3')
l.next.next.next = ListNode('4')
h = swapPairs(l)
print(h.val)
print(h.next.val)
print(h.next.next.val)
print(h.next.next.next.val)