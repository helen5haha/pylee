'''
Given a linked list, determine if it has a cycle in it.
Can you solve it without using extra space?
'''

def hasCycle(head):
    if None == head:
        return False
    fast = slow = head
    while True:
        fast = fast.next
        if None == fast:
            return False
        fast == fast.next
        if None == fast:
            return False
        slow = slow.next
        if fast == slow:
            return True